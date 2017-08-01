#!/usr/bin/env python
# -*- coding: gbk -*-
# @Time    : 2017/5/23 19:25



import urllib2,cookielib,urllib
# headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# 'Connection':'keep-alive',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
#
# }
# req = urllib2.Request('http://blog.csdn.net/cqcre',headers=headers)
# try:
#     print urllib2.urlopen(req).read()
# except urllib2.HTTPError as e:
#     print e
#     print e.code
#     print e.reason
# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print 'name = ',item.name
#     print 'value = ',item.value
# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# postdata = {'username':'wz74666291','password':'qq74666291',
#             'code':{
#                 'lt':'LT-578253-BjkwkmbpPmZMLC7OdE3Nbib97cRE03',
#                 'execution':'e1s1',
#                 '_eventId':'submit',
#                 'submit':'登陆'}
# }
# postdata = urllib.urlencode(postdata)
# header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
# url = 'https://cas.xjtu.edu.cn/login'
# res = urllib2.Request(url,postdata)
# response = opener.open(res)
# cookie.save(filename,ignore_discard=True,ignore_expires=True)
# cookie.load(filename,ignore_discard=True,ignore_expires=True)
# # response2 = opener.open('http://ssfw.xjtu.edu.cn')
# res = urllib2.Request('https://cas.xjtu.edu.cn/login?service=http%3A%2F%2Fssfw.xjtu.edu.cn%2Findex.portal',data=postdata,headers=header)
# text = urllib2.urlopen(res)
# print text.read()

# url = 'http://www.qiushibaike.com/hot/'
#
# try:
#     header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
#     request = urllib2.Request(url,headers=header)
#     response = urllib2.urlopen(request)
#     pat = '<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>'
#     print response.read()
# except urllib2.URLError, e:
#     if hasattr(e,"code"):
#         print e.code
#     if hasattr(e,"reason"):
#         print e.reason

import sys,re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

#
driver = webdriver.Chrome()
driver.get('http://ssfw.xjtu.edu.cn')
# assert 'Python' in driver.title
elem = driver.find_element_by_name("username")
elem.send_keys('wz74666291')
elem2 = driver.find_element_by_name("password")
elem2.send_keys('qq74666291')
elem2.send_keys(Keys.RETURN)


del elem,elem2
driver.implicitly_wait(10)
# assert '欢迎访问西安交通大学师生服务首页'.decode('gbk') in driver.title
elem = driver.find_element_by_id('pp1142_p1144')
elem.click()
driver.implicitly_wait(1)
elem2 = driver.find_element_by_id('pp1142_p1144_p1156')
elem2.click()

page = driver.page_source.decode('utf-8')
pat = re.compile(r'<a.*?onclick="newFamily\(\'([0-9]+?)\'',re.S)
pat2 = re.compile('<td class="">(.*?)</td>',re.S)
print page
print re.findall(pat,page)
print [str(i).decode('utf-8') for i in re.findall(pat2,page)]
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# class PythonOrgSearch(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys('pycon')
#         elem.send_keys(Keys.RETURN)
#         assert "No results found" not in driver.page_source
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == '__main__':
#     unittest.main()