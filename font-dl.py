#!/usr/bin/env python
#encoding: utf-8

from urllib import *
from urlparse import *
import re, sys

class DownloaderError(Exception):
    def __init__(self, msg=False):
        self.msg = msg

class fontdl():
    def __init__(self, url):
        self.url = url
        self.response = urlopen(url)

        # checks if the css file exists.
        if self.response.getcode() != 200:
            raise DownloaderError('\nError al conectar con el servidor: %d' % self.response.getcode())

    # def cssDownloader(self):
    #     # search inside the css file for the fonts files and download them.
    #     html = self.response.read()
    #     pattern = "(https?.\/\/)?([a-z\d\.-]+\.[a-z\.]{2,6})([\/a-z\s\.-]+)\/([a-z\d\.-]+\.(woff|eot|ttf|otf|svg))"
    #     fonts = re.finditer(pattern, html)

    #     for font in fonts:
    #         url = font.group()
    #         filename = font.group(4)
    #         print ("Descargando archivo: %s" % filename)
    #         urlretrieve(url, filename)

    def fontSearch(self):
        # search inside the css file for the fonts files.
        html = self.response.read()
        pattern = "(https?.\/\/)?([a-z\d\.-]+\.[a-z\.]{2,6})?([\/\w\s\.-]+)\/([\w\.-]+\.(woff|tff|otf|ttf))"
        self.fontsUrl = re.finditer(pattern, html)


    def fontDownloader(self):
        # Checks if the url is absolute or relative, if it's relative builds an absolute url. And downloads the font.
        for item in self.fontsUrl:
            if item.group(2) == None:
                DownloadUrl = urljoin(self.url, item.group())
            else:
                DownloadUrl = item.group()
                
            filename = item.group(4)
            print("Descagando archivo: %s" % filename)
            urlretrieve(DownloadUrl, filename)


url = sys.argv[1]
a = fontdl(url)
a.fontSearch()
a.fontDownloader()