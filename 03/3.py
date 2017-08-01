#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/11 18:27
from activate import new_activation
import redis
# import sqlite3
activate_list = []
for i in range(100):
    activate_list.append(new_activation(20))
# if os.path.exists('./active.db'):
#     os.remove('./active.db')
# conn = sqlite3.connect('./active.db')
r = redis.Redis(host='localhost',port=6379,db=0)
r.set('activate',activate_list)
print r.get('activate')
# cursor = conn.cursor()
# sql = '''CREATE TABLE `activate`(\
#          `ID` integer PRIMARY KEY NOT NULL,\
#          `ACTIVATE_CODE` char(20) NOT NULL )'''
# cursor.execute(sql)
# conn.commit()


# try:
#     for i in range(100):
#         sql1 = "INSERT INTO ACTIVATE (ACTIVATE_CODE) VALUES ('%s')"%activate_list[i]
#         print sql1
#         cursor.execute(sql1)
# except Exception as e:
#     raise e
# finally:
#     sql2 = 'select * from activate'
#     cursor.execute(sql2)
#     print cursor.fetchall()
#     conn.commit()
#     cursor.close()
#     conn.close()
