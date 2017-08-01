#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 19:41
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont
pic = Image.open('a.jpg')
location = (40,40)
text = 'a'
# fnt = ImageFont.
draw = ImageDraw.Draw(pic)
font = ImageFont.truetype("arial.ttf", 500)
draw_text = draw.text(xy=location,text=text,fill='red',font=font)
pic.show()
pic.save('b.jpg')
# draw.show()
# draw.save('b.jpg')
