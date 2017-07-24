#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 15:42

import csv,json,xlwt
import os




def read_json(filename):
    return json.loads(open(filename).read().encode('gbk'))


def write_to_csv(data,filename):

    dw = xlwt.Workbook()
    ws = dw.add_sheet("student",cell_overwrite_ok=True)
    row = 0
    col = 0
    print(data.items())
    for k,v in sorted(data.items(), key=lambda d:d[0]):
        ws.write(row, col, k)
        for i in v:
            col = col+1
            ws.write(row,col,i)
        row+=1
        col=0
    if os.path.exists(filename):
        os.remove(filename)
    dw.save(filename)

print('请求索引页出错')
write_to_csv(read_json('a.txt'),'student.xls')