import os
import bs4
import requests
from sys import *
from urllib.request import urlopen


def ImageUrlScrapper(url):
    connection = urlopen(url)
    raw_html = connection.read()
    # print(raw_html)
    connection.close()
    page_soup = bs4.BeautifulSoup(raw_html, "html.parser")
    # print(page_soup)
    container = page_soup.findAll("div", {"class": "item-container"})
    return container


def main():
    if (len(argv) == 2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("this Application is designed for Download the file")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : give us a link Download the file ")
            exit()
    try:
        url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?TpK=video%20card"
        listout = ImageUrlScrapper(url)
        print("Urls of all images")
        for elements in listout:
            print(elements.a.img['data-src'])
    except Exception as e:
        print("INvalid option", e)


if __name__ == '__main__':
    main()
