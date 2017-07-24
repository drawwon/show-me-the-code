#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/21 13:03
# import re,os,threading
# import urllib2,urllib,socket
# from PIL import Image
# class getimagethread(threading.Thread):
#     def __init__(self,url,filename):
#         threading.Thread.__init__(self)
#         self.url = url
#         self.filename = filename
#     def run(self):
#         try:
#             mutex.acquire()
#             print self.url
#             mutex.release()
#             urllib.urlretrieve(self.url, self.filename)
#         except:
#             pass
#
# mutex = threading.Lock()
# socket.setdefaulttimeout(5)
# text = urllib2.urlopen('https://www.zhihu.com/question/23535321').read()
# pat = re.compile(r'src="(http[s]?://.+?\.jp[e]?g)"',re.I)
# links = re.findall(pat, text)
# # print links
# if not os.path.exists(r'.\pic'):
#     os.makedirs(r'.\pic')
# thread = []
# for i, url in enumerate(set(links)):
#     # print url
#     filename = r'.\pic\%s.jpg'%i
#     thread.append(getimagethread(url,filename))
#
# for t in thread:
#     t.start()
# for t in thread:
#     t.join()
# print 'done'

import urllib2,re,os,sys,threading
from bs4 import BeautifulSoup
url = 'https://www.zhihu.com/question/38643401'
if not os.path.exists(r'.\pic'):
    os.makedirs(r'.\pic')
def useragent(url):
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 36.0.1985.125 Safari / 537.36",\
    "Referer": 'http://baidu.com/'}
    req = urllib2.Request(url, headers=i_headers)
    html = urllib2.urlopen(url).read()
    return html
def getpageimg(url):
    try:
        html = useragent(url)
        soup = BeautifulSoup(html)
        for imgurl in soup.findAll('div', style='padding-top: 5px;')
            img = imgurl.find
