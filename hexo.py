#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/10 19:42

import os
hexo_way = 'E:\项目\blog'
os.system('cd '+hexo_way)
os.system('hexo d -g')
os.system(ur'git add .')
os.system("git commit -m 'Updated'")
os.system('git push origin source')
print 'done'