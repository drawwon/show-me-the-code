#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/11 22:21
import re
from string import punctuation
with open(raw_input('filename:')) as f:
    text = f.read()
    punctuation = punctuation+' '
    pat = '[%s]+' % punctuation
    word = re.split(pat,text)
    print word
    print len(set(word))
