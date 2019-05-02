import os
import requests
from sys import *
from urllib.parse import urlparse


def is_downloadble(url):
    h = requests.head(url, allow_redirect=True)
    header = h.header
    content_type = header.get("content_type")

    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def get_filename_from_cd(cd):
    a = urlparse(cd)
    return os.path.basename(a.path)
