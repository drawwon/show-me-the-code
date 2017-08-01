#!/usr/bin/env python
# -*- coding: gbk -*-
# @Time    : 2017/5/14 18:31
import os

if __name__ == '__main__':
    list_dir = os.walk(raw_input("dictionary name:"))
    pat = '\n'
    code_num = 0
    annotation_num = 0
    for root, dirs, files in list_dir:
        for f in files:
            file_name = os.path.join(root,f)
            with open(file_name) as ff:
                text = ff.read()
                sentence = text.split(pat)
                for line in sentence:
                    if line.strip().startswith('#') or line.strip() == '':
                        annotation_num = annotation_num + 1
                    else:
                        code_num += 1
    print annotation_num
    print code_num


