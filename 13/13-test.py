#!/usr/bin/env python
# -*- coding: gbk -*-
# @Time    : 2017/5/20 14:33
import os
from PIL import Image
try:
    with Image.open(r'.\pic\0.jpg') as f:
        pass
except:
    os.remove(r'.\pic\0.jpg')
