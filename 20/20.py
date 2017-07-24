#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/27 16:50

import xlrd,re,pprint
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
import seaborn
wb = xlrd.open_workbook('2017-6.xls')
ws = wb.sheet_by_index(0)


def time2second(time):
    second_pattern = u'([0-9]+)秒'
    minute_pattern = u'([0-9]+)分'
    minute = re.findall(minute_pattern, time)
    second = re.findall(second_pattern, time)
    # print minute,second
    if minute:
        return int(minute[0]) * 60 + int(second[0])
    else:
        if second:
            return int(second[0])
        else:
            return 0




data=[]
for i in range(ws.nrows):
    data.append(ws.row_values(i))
data.pop(0)
call_num = OrderedDict()
call_time = OrderedDict()
month = '2017-06-'
day_range = range(1,31)
for i,item in enumerate(day_range):
    if item < 10:
        day_range[i] = '0'+str(item)
    else:
        day_range[i] = str(i)
date_range = [ month + day + " " for day in day_range]
for date in date_range:
    call_num[date] = 0
    call_time[date] = 0
for row in range(len(data)):
    row_value = data[row]
    time = time2second(row_value[3])
    for element in row_value:
        for date in date_range:
            if re.match(date,element):
                # print element
                call_num[date] = call_num[date] + 1
                call_time[date] = call_time[date] + time
# print call_num
# print call_time
num = []
time = []
for i in call_num.iteritems():
    num.append(i[1])
    time.append(i[0])
print num
print np.arange(len(num))
plt.bar(np.arange(len(num)),num)
plt.xticks(range(len(num)))
for i, v in enumerate(num):
    plt.text(i-0.35,v+0.2, str(v), color='blue', fontweight='bold')
plt.show()

