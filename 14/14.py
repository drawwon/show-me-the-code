#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 15:42

import csv,json,xlwt
import os




def read_json(filename):
    # return json.loads(open(filename).read().encode('gbk'))
    print type(open(filename).read().decode('gbk'))
    return json.loads(open(filename).read().decode('gbk'))


def zhprint(obj):
    import re
    print re.sub(r"\\u([a-f0-9]{4})", lambda mg: unichr(int(mg.group(1), 16)), obj.__repr__())

def write_to_csv(data,filename):

    dw = xlwt.Workbook()
    ws = dw.add_sheet("student",cell_overwrite_ok=True)
    row = 0
    col = 0
    print json.dumps(data.items(),ensure_ascii=False)
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


write_to_csv(read_json('a.txt'),'student.xls')
print 'done'