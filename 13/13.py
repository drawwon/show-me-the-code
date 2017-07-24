#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/20 14:11
import re,os
import urllib2,urllib,socket
from PIL import Image

text = urllib2.urlopen('https://www.zhihu.com/question/23535321').read()
pat = re.compile(r'src="(http[s]?://.+?\.(jp[e]?g|png))"')
# pat2 = re.compile(r'src="(.+?\.png)"')
links = re.findall(pat, text)
socket.setdefaulttimeout(10)
print links
links = set(links)
# links2 = re.findall(pat2, text)
# print len(links2)
if not os.path.exists(r'.\pic'):
    os.makedirs(r'.\pic')
for i,p in enumerate(links):
    try:
        # print p[0]
        urllib.urlretrieve(p[0],r'.\pic\%s.jpg'%i)
        print '%s.jpg is downloading'%i
    except:
        print '%s.jpg download fail' % i
        pass

# for root,dic,files in os.walk(r'.\pic'):
#     for f in files:
#         try:
#             print os.path.join(root,f)
#             pic = Image.open(os.path.join(root,f))
#             width,height = pic.size
#             pic.close()
#             if width<100 or height<100:
#                 os.remove(os.path.join(root,f))
#         except IOError as e:
#             os.remove(os.path.join(root, f))