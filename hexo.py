#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/10 19:42

import os
hexo_way = ur'E:\项目\blog'
print 'cd ' + hexo_way
os.system(ur'cd E:\项目\blog \n'.encode('gbk')+'dir')
os.system('hexo d \-g')
os.system(ur'git add .')
os.system("git commit -m 'Updated'")
os.system('git push origin source')
print 'done'