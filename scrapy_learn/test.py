#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 19:46
import re,bs4
with open('a.html') as f:
    text = f.read()
# text = open('a.html','r').read()
print text
pat = re.compile(r'<a.*?\;([0-9]+?)&#',re.S)
pat2 = re.compile(r'<td class=\"\">\n(.*?)</td>',re.S)
print re.findall(pat,text)
print [str(i) for i in re.findall(pat2,text)]