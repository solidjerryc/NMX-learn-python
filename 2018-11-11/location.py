#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:02:27 2018

@author: caiboqin
"""

import pandas as pd
import requests
import json #解析json字符串，用于各种api，可以将高德得到的json字符串转换成字典
import urllib
from tqdm import tqdm#需要自行安装 pip install tqdm

df=pd.read_csv('nanjing.csv')
name=df['name'].drop_duplicates()

key='4cded7abcbaf4dc2b8eb4789fbb886e2'
#addr=urllib.request.quote('南京大学')
#url='http://restapi.amap.com/v3/geocode/geo?key=4cded7abcbaf4dc2b8eb4789fbb886e2&address='+addr+'&city=%E5%8D%97%E4%BA%AC'
#
#req=requests.get(url)
#a=req.text
#b=json.loads(a)
#lng,lat=b['geocodes'][0]['location'].split(',')

def getlocation(name):
    addr=urllib.request.quote(name)#将中文汉字转换成网页链接可以识别的编码
    url='http://restapi.amap.com/v3/geocode/geo?key='+key+'&address='+addr+'&city=%E5%8D%97%E4%BA%AC'
    req=requests.get(url)
    a=req.text
    b=json.loads(a)#解析json字符串，用于各种api，可以将高德得到的json字符串转换成字典
    lng,lat=b['geocodes'][0]['location'].split(',')
    
    return(lng,lat)

c=[]
d=[]
for i in tqdm(name):#循环列表中的每一个元素
    try:
        lng,lat=getlocation(i)
    except:
        lng=0
        lat=0
#        try语句块，用于处理运行异常，此处表示当输入name时，无法找到对应经纬度，赋予该经纬度为0
    c.append(lng)
    d.append(lat)
e=pd.DataFrame({'name':name,'lng':c,'lat':d})


f=df.merge(e,how='left',on='name')





