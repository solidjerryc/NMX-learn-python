#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 13:53:26 2018

@author: caiboqin
"""

import requests
import pandas as pd
from lxml import etree 
from tqdm import tqdm

url='http://nanjing.esf.fang.com/house/i31/'

header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

#req=requests.get(url,headers=header)
##req.encoding='utf8'#如果乱码加这行指定一下编码类型 可选参数有 utf8、gbk
#html=req.text
def finddata(html_string, xpath):
    tree=etree.HTML(html_string)
    return tree.xpath(xpath)

#total=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[2]/span/b/text()')
#unit=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[2]/span[2]/text()')
#
#name=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[1]/p[2]/a/@title')
#location=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[1]/p[2]/span/text()')
#a=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[1]/p[1]/text()')
#title=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[1]/h4/a/@title')
#
#unit_new=[i.split('元')[0] for i in unit]
#df=pd.DataFrame({'title':title,'name':name,'location':location,'total':total,'unit':unit_new})

def findpage(url):
    req=requests.get(url,headers=header)
#req.encoding='utf8'#如果乱码加这行指定一下编码类型 可选参数有 utf8、gbk
    html=req.text
    total=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[2]/span/b/text()')
    unit=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[2]/span[2]/text()')
    name=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[1]/p[2]/a/@title')
    location=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[1]/p[2]/span/text()')
#    a=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[1]/p[1]/text()')
    title=finddata(html,'//div[@class="shop_list shop_list_4"]/dl/dd[1]/h4/a/@title')

    unit_new=[int(i.split('元')[0]) for i in unit]
    #列表推导式，通过元分割字符串，删除后面的乱码并将字符串格式转换成数字
    df=pd.DataFrame({'title':title,'name':name,'location':location,'total':total,'unit':unit_new})
    return df

a=pd.DataFrame()
#for x in range(1,11):
#    print(x)#显示运行到第几页
#    b=findpage('http://nanjing.esf.fang.com/house/i3%s/'%x)
#    a=pd.concat([a,b],axis=0)
    
for x in tqdm(range(1,101)):# 进度条
    b=findpage('http://nanjing.esf.fang.com/house/i3%s/'%x)
    a=pd.concat([a,b],axis=0)#纵向合并数据框
    
a=a.drop_duplicates()

a.to_csv('nanjing.csv',index=None)





