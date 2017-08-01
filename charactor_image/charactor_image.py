#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 20:46

from PIL import Image
import argparse
from string import punctuation
import getopt,sys
import numpy as np


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

# def transPNG(src_img, dst_img):
#     img = Image.open(src_img)
#     assert isinstance(img,Image.Image)
#     img = img.convert('RGBA')
#     datas = img.getdata()
#     newdata = list()
#     for i,item in enumerate(datas):
#         if i ==1 or i==2 or i==3:
#             print item
#         if item[0] == 3 and item[1] == 121 and item[2] == 182 :
#             newdata.append((0,0,0,0))
#         else:
#             newdata.append(item)
#
#     img.putdata(newdata)
#     img.save(dst_img,'png')

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
    in_file_name = 'wz.png'
    out_file_name = 'xue.txt'
    for opt,value in opts:
        if opt == '-i':
            in_file_name = value
        if opt == '-o':
            out_file_name = value
        elif opt == 'h':
            print u'用法：-i 输入文件名 -o 输出文件名'
    # transPNG(in_file_name,'xue1.png')
    im = Image.open(in_file_name)
    assert isinstance(im, Image.Image)
    width, height = im.size
    im = im.resize((int(width/10),int(height/10)),Image.ANTIALIAS)
    width, height = im.size

    print width,height
    txt = ''
    for i in xrange(height):
        for j in xrange(width):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    with open(out_file_name,'w') as f:
        f.write(txt)