#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:48:44 2018

@author: caiboqin
"""

import requests

#url='http://www.cjh.com.cn/'
#
#req=requests.get(url)
##req.text  读取网页代码
#html=''
#if req.status_code==200:
#    html=req.text
#    print(html)
#elif req.status_code//100==4:
#    print('client error')
#elif req.status_code//100==5:
#    print('server error')


url='http://nweb.cjh.com.cn/sssqold.html'

header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'https://cn.bing.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}#假装自己是以浏览器访问，在开发者工具里面找到network里面的requestheaders的信息 复制进来然后修改成字典的格式

req=requests.get(url,headers=header)
html=req.text
print(html)