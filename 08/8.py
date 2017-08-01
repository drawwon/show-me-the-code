#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/17 17:11
import re
from bs4 import BeautifulSoup
import urllib2
from readability import Document
html = urllib2.urlopen('https://github.com/drawwon/show-me-the-code')#(raw_input('please input the file name:'))
text = html.read()
doc = Document(text)
print doc.content()

# text = BeautifulSoup(html,'lxml').prettify()
# pat = re.compile( r'<body.*?>(.+)<\/body>', re.DOTALL)
# a = re.findall(pat, text)
# print a
# for line in a:
#     print type(line)
#     pat2 = re.compile(r'[\t\n]+?')
#     b = re.split(pat2, line)
# # print type(b)
# # print len(b)
# for i in b:
#     print i
# f = open('a.txt','a+')
# for i in b:
#     f.write(i.encode('utf-8'))
# f.close()

