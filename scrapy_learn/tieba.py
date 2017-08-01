#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/24 20:43
import urllib2,urllib,re

class Tool:
    def __init__(self):
        #去除img标签,7位长空格
        self.removeImg = re.compile('<img.*?>| {7}|')
        #删除超链接标签
        self.removeAddr = re.compile('<a.*?>|</a>')
        #把换行的标签换为\n
        self.replaceLine = re.compile('<tr>|<div>|</div>|</p>')
        #将表格制表<td>替换为\t
        self.replaceTD= re.compile('<td>')
        #把段落开头换为\n加空两格
        self.replacePara = re.compile('<p.*?>')
        #将换行符或双换行符替换为\n
        self.replaceBR = re.compile('<br><br>|<br>')
        #将其余标签剔除
        self.removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

class BDcrawler:
    def __init__(self,baseurl,seeLZ):
        self.baseurl = baseurl
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = Tool()

    def getpage(self,pageNum):
        try:
            url = self.baseurl+self.seeLZ+'&pn='+str(pageNum)
            req = urllib2.Request(url)
            text = urllib2.urlopen(req).read()
            return text
        except Exception as e:
            print '连接失败' + e

    def Checkresult(self,result):
        if result:
            return result
        else:
            return None

    def getTitle(self):
        page = self.getpage(1)
        pat_title = re.compile('<title>(.*?)</title>', re.S | re.I)
        result = re.search(pat_title, page).group(1)
        return self.Checkresult(result)

    def getPagenum(self):
        page = self.getpage(1)
        pat_pagenum = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pat_pagenum,page).group(1)
        return self.Checkresult(result)

    def getContent(self,pageNum):
        content_pat = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(content_pat, self.getpage(pageNum))
        # for item in items:
        #     print item
        print self.Checkresult(self.tool.replace(items[0]))


if __name__ == '__main__':
    baseurl = 'http://tieba.baidu.com/p/5053944826'
    bac = BDcrawler(baseurl,0)
    bac.getContent(1)
