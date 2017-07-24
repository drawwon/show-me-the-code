#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 21:28

import xlwt,json
def red_tet_to_xlsfile(txtfile,xlsfile):
    with open(txtfile) as f:
        data = json.loads(f.read().encode('utf-8'))

    wb = xlwt.Workbook()
    sheet = wb.add_sheet('num')
    row = col = 0
    print(data)
    for i in data:
        for j in i:
            sheet.write(row,col,j)
            col = col+1
        row = row+1
        col = 0
    wb.save(xlsfile)

if __name__ == '__main__':
    red_tet_to_xlsfile('number.txt','number.xls')