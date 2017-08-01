#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/19 18:59
import codecs
import re
import chardet
b_list = ['北京','程序员','公务员','领导','牛比','牛逼','你娘','你妈','love','sex','jiangge']
# with codecs.open('a.txt','r','utf-8') as f:
#     text =  f.read()
#     print text
text = open('a.txt').read().decode('utf-8')
pat_f = ''
for i in b_list:
    pat_f = pat_f + '[' + i + ']' + '+'
# pat_f = pat_f.encode('utf-8', 'unicode')
# b = re.findall(u'(北京)+', text)
pat_f = pat_f.decode('utf-8')
print type(pat_f)
print type(text)
for i in b_list:
    pat = str('('+ i +')' + '+').decode('utf-8')
    text = re.sub(u'%s'%pat, u'*'*(len(pat)-3), unicode(text))
# a = re.sub(pat_f, '*', text)
# print a
print text
# print ''.join(b).encode('utf-8','gbk')