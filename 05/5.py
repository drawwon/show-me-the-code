#!/usr/bin/env python
# -*- coding: gbk -*-
# @Time    : 2017/5/12 18:58

import os
from PIL import Image
def resize(filename,new_name):
    pic = Image.open(filename)
    out = pic.resize((100,200),Image.ANTIALIAS)
    out.save(new_name,quality=100)

list_dir = os.walk(r'C:\Users\jeffrey\Desktop\python exercise\python练习册\5\pic')
for root, dirs, files in list_dir:
    for f in files:
        a = os.path.join(root, f)
        print a
        new_name = os.path.join(root,'new_1'+f)
        print new_name
        resize(a,new_name)
