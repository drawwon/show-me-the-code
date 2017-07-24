#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/10 17:09
import xlrd,json
from xml.dom import minidom


# def list2dict(list_name):
#     dic = {}
#     for list_element in list_name:
#         dic[list_element[0]] = list_element[1:]
#     return dic

def creat_and_write_xml(filename,row_data):
    xml = minidom.Document()
    root = xml.createElement('root')
    xml.appendChild(root)
    student = xml.createElement('student')
    root.appendChild(student)
    student.appendChild(xml.createComment("学生信息表\"id\" : [名字, 数学, 语文, 英文]"))
    row_data = json.dumps(row_data)

    text = xml.createTextNode(str(row_data))

    student.appendChild(text)
    f = open(filename,'wb')
    f.write(xml.toprettyxml())
    f.close()



if __name__ == '__main__':
    data = xlrd.open_workbook('student.xls')
    table = data.sheet_by_index(0)
    row_data = {}
    for i in range(table.nrows):
        # print(i)
        row_data[i+1] = table.row_values(i)[1:]
    print row_data
    filename = 'student.xml'
    creat_and_write_xml(filename, row_data)