#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/14 18:59

import os
list_dir = os.walk('.')
for root,dic,files in list_dir:
    print 'root%s'%root
    print files