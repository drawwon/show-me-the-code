#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/18 16:24
from __future__ import division
import string
import random
from PIL import ImageDraw
from PIL import Image,ImageFont,ImageFilter
l = []
num = 4
for j in range(num):
    l.append(random.choice(string.letters+''.join([str(i) for i in range(10)])))
pic = Image.new('RGB',(500,200),0xffff)
draw = ImageDraw.Draw(pic)
color2 = ['Lavender','LightGrey','LightSlateGray']
color1 = ['BurlyWood','DarkGray','Gray']
width, height = pic.size
for i in range(width+1):
    for j in range(height+1):
        draw.point(xy=(i,j),fill=random.choice(color1))



font = ImageFont.truetype("arial.ttf", 100)
for i in range(len(l)):
    x = i*width/num+5
    c = random.choice(color2)
    draw.text(xy=(x,50),text=l[i],fill=c,font=font)

pic = pic.filter(ImageFilter.BLUR)
pic.show()
pic.save('a.jpg')