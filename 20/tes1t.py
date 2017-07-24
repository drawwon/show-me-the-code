#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/27 17:24
import re
time = '1分32秒'
def time2second(time):
    second_pattern = '([0-9]+)秒'
    minute_pattern = '([0-9]+)分'
    minute = re.findall(minute_pattern,time)
    second = re.findall(second_pattern,time)
    print minute,second
    print minute,second
    if minute:
        return int(minute[0])*60 + int(second[0])
    else:
        return int(second[0])
print time2second(time)