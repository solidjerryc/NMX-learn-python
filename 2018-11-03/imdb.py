#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 18:00:14 2018

@author: caiboqin
"""

import requests
import pandas as pd
from lxml import etree 
url='https://www.imdb.com/chart/top'
header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'https://cn.bing.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}#假装自己是以浏览器访问，在开发者工具里面找到network里面的requestheaders的信息 复制进来然后修改成字典的格式

req=requests.get(url,headers=header)
html=req.text
imdb=etree.HTML(html)
title=imdb.xpath('//tbody[@class="lister-list"]/tr/td[2]/a/text()')
year=imdb.xpath('//tbody[@class="lister-list"]/tr/td[2]/span/text()')
score=imdb.xpath('//tbody[@class="lister-list"]/tr/td[3]/strong/text()')

year_new=[i[1:5] for i in year]#利用列表推导式把year列表中两边的括号去掉

df=pd.DataFrame({'title':title,'year':year_new,'score':score})
df.to_csv('test1.csv',index=None)



