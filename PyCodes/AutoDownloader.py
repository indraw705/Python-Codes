import os
import requests
from sys import *
from urllib.parse import urlparse


def is_downloadble(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get("content-type")
    print("++++++\n", content_type)
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def get_filename_from_cd(cd):
    a = urlparse(cd)
    return os.path.basename(a.path)


def fileDownloader(url):
    allowed = is_downloadble(url)
    if allowed:
        try:
            res = requests.get(url, allow_redirects=True)
            filename = get_filename_from_cd(url)
            fd = open(filename, "wb")
            for buffer in res.iter_content(1024):
                fd.write(buffer)
            fd.close()
            return True
        except Exception as e:
            return False
    else:
        return False


def main():
    print("fileDownloader indrajit Narvekar")
    if (len(argv) == 2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("this Application is designed for Download the file")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : give us a link Download the file ")
            exit()
    # url = "https://www.google.com/favicon.ico"
    url = "https://www.souravsengupta.com/cds2015/python/LPTHW.pdf"
    result = fileDownloader(url)
    if result:
        print("File Downloaded successfully")
    else:
        print("Failed to Download")


if __name__ == '__main__':
    main()
