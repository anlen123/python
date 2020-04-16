#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   文件批量重命名.py
@Time    :   2019/12/16 22:07:48
@Author  :   刘华强
@Contact :   1761512493@qq.com
'''
import parsel
import requests
import re 
from lxml import etree
def dailichi():
    import random
    daili = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; WOW64; Trident/4.0; SLCC1)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    ]
    dai = random.choice(daili)
    # print(dai)
    head  ={
        'User-Agent':'%s'% dai
    }
    return head


def down_page(url):
    response = requests.get(url=url,headers=dailichi())
    txt = response.text
    sel = parsel.Selector(response.text)
    title = sel.xpath('//ul[@class="bigimg cloth_shoplist"]//li/a/@title').getall()
    price = sel.xpath('//ul[@class="bigimg cloth_shoplist"]//li/p[@class="price"]/span/text()').getall()
    # item = dict(zip(title,price))
    # print(item)
    for i,j in zip(title,price):
        i = i.replace(' ','')
        with open('当当网前50页.txt','a+',encoding="utf-8")as f:
            f.writelines(str(i)+":"+str(j)+'\n')
def get_url_list():
    url_list=[]
    [url_list.append('http://category.dangdang.com/pg%s-cid4011007.html'%(str(i))) for i in range(1,51)]
    return url_list
def duoxiancheng(Hanshu,List,Time):
   import time
   from concurrent.futures import ThreadPoolExecutor
   pool= ThreadPoolExecutor(max_workers=10)
   for i in List:
   pool.submit(Hanshu,i)
   time.sleep(Time)
   pool.shutdown()

url_list= get_url_list()
print(url_list)
duoxiancheng(down_page,url_list,0)
# down_page(url_list[0])