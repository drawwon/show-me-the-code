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
    number = xml.createElement('number')
    root.appendChild(number)
    number.appendChild(xml.createComment("城市信息"))
    row_data = json.dumps(row_data,ensure_ascii=False)

    text = xml.createTextNode(row_data.encode('utf-8'))

    number.appendChild(text)
    f = open(filename,'wb')
    f.write(xml.toprettyxml())
    f.close()



if __name__ == '__main__':
    data = xlrd.open_workbook('number.xls')
    table = data.sheet_by_index(0)
    row_data = {}
    # res=[]
    # for i in range(table.nrows):
    #     for j in range(table.ncols):
    #         if isinstance(table.cell(i,j).value,unicode):
    #             a = table.cell(i,j).value.encode('gb2312')
    #             # print table.cell(i,j).value
    #         elif isinstance(table.cell(i,j).value,float) or isinstance(table.cell(i,j).value, int):
    #             a = unicode(table.cell(i,j).value).decode('utf-8').encode('gb2312')
    #             # print table.cell(i, j).value
    #
    #         # table.cell(i, j).value = str(table.cell(i, j).value).decode('utf-8').encode('gb2312')
    #         res.append(a)
    #     res.append("|")
    # # print res
    # res_string = ' '.join(res).split("|")
    # res_string.pop(-1)
    # print res_string,'11111111112'
    # for i in range(len(res_string)):
    #     row_data[i+1] = res_string[i][1:]
    # print row_data
    for i in range(table.nrows):
        # print(i)
        row_data[i+1] = table.row_values(i)[1:]
    filename = 'number.xml'
    creat_and_write_xml(filename, row_data)