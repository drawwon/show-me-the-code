#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/25 15:02

import re,json
import requests
import urllib
from bs4 import BeautifulSoup

def get_page_index(offset,keyword):
    data={
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoload':'true',
        'count':'20',
        'cur_tab':1}
    url = 'https://www.toutiao.com/search_content/?' + urllib.urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print e
        return None

def pharse(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print e
        return None

def get_parse_page_data(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    image_pattern = re.compile('var gallery = (.*?);',re.S)
    image_pattern2 = re.compile('<img src="(.*?)"')
    result = re.search(image_pattern,html)
    result2 = re.findall(image_pattern2, html)
    if result:
        data = result.group(1)
        data = json.loads(data)
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            return {
                'title':title,
                'url':url,
                'images':images
            }
    # if result2:
    #     print result2

def main():
    html = get_page_index(0,'街拍')
    for url in pharse(html):
        html = get_page_detail(url)
        if html:
            print get_parse_page_data(html,url)
    # print html




if __name__ == '__main__':
    main()