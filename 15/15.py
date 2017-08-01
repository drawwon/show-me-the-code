#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 20:42

import xlwt,json



def excel_write(txtfile, csvfile):
    with open(txtfile) as f:
        data = json.loads(f.read().encode('gbk'))
    cs = xlwt.Workbook()
    shet = cs.add_sheet('student',cell_overwrite_ok=True)
    row = 0
    col = 0
    for i,j in data.items():
        shet.write(row,col,i)
        shet.write(row,col+1,j)
        row += 1
        col = 0
    cs.save(csvfile)

if __name__ == '__main__':
    excel_write('a.txt','student.xls')
