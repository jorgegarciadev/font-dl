#!/usr/bin/env python
#encoding: utf-8

from urllib import *
import re, sys

class DownloaderError(Exception):
    def __init__(self, msg=False):
        self.msg = msg

class fontDownloader():
    def __init__(self, url):
        self.url = url
        self.response = urlopen(url)

        # checks if the css file exists.
        if self.response.getcode() != 200:
            raise DownloaderError('\nError al conectar con el servidor: %d' % self.response.getcode())

    def cssDownloader(self):
        # search inside the css file for the fonts files and download them.
        html = self.response.read()
        pattern = "(https?.\/\/)?([a-z\d\.-]+\.[a-z\.]{2,6})([\/a-z\s\.-]+)\/([a-z\d\.-]+\.(woff|eot|ttf|otf|svg))"
        fonts = re.finditer(pattern, html)

        for font in fonts:
            url = font.group()
            filename = font.group(4)
            print ("Descargando archivo: %s" % filename)
            urlretrieve(url, filename)


url = sys.argv[1]
a = fontDownloader(url)
a.cssDownloader()
