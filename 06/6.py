#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 20:24
import re
from string import punctuation
with open('a.txt') as f:
    text = f.read()
    punctuation = punctuation+' '
    pat = '[%s]+' % punctuation
    word = re.split(pat,text)
    w = {}
    for w1 in word:
        count = 0
        for w2 in word:
            if w1 == w2:
                count += 1
        w[w1]=count
    print w
    cou = 0
    for key,value in w.iteritems():
        if value > cou:
            cou = value
            key_temp = key
print key_temp