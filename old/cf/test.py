# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  刘华强
@Version        :  
------------------------------------
@File           :  文件批量重命名.py
@Description    :  
@CreateTime     :  2019/11/28 10:36
------------------------------------
@ModifyTime     :  
"""
import requests
import parsel
import os

def get_name_url():
    file = open('./name.csv','r')
    txt = file.read()
    txt = txt.split('\n')
    url_list = []
    name_list = []
    for x in txt[1:-1]:
        x = x.split(',')
        url_list.append(x[0])
        name_list.append(x[1])
    return url_list,name_list
def get_changshu(url):
    response = requests.get(url)
    sle = parsel.Selector(response.text)
    tt = sle.xpath('//*[@id="pageContent"]/div[3]').re('\<td\>(\d*)\<\/td\>\\r\\n                \<td\>\\r\\n                    \<a href\=\".*?\" title\=\"(.*?)\"\>\\r\\n.*?\<\/a\>\\r\\n                \<\/td\>\\r\\n                \<td\>\\r\\n                        \<a href\=\".*?"\>\\r\\n\ *(\d*)\\r\\n                        \<\/a\>\\r\\n                \<\/td\>\\r\\n                \<td\>\\r\\n                    \<a href\=\".*?\"\>\\r\\n\ *(\d)\\r\\n                    \<\/a\>\\r\\n                \<\/td\>\\r\\n                \<td\>\\r\\n                    \<span style\=\".*?\"\>(.*?)\<\/span\>\\r\\n                \<\/td\>\\r\\n                \<td\>\\r\\n\ *(\d*)\\r\\n                \<\/td\>\\r\\n                \<td\>')
    b = [tt[i:i+6] for i in range(0,len(tt),6)]
    for x in b[::-1]:
        with open('ans.csv','a+')as f:
            for y in x:
                f.write(y)
                f.write(',')
            f.write('\n')
    with open('ans.csv', 'a+')as f:
        f.write('\n\n\n\n\n')
url_list,name_list = get_name_url()
for x,y in zip(url_list,name_list):
    url = 'http://codeforces.com/contests/with/'+str(x)
    with open('ans.csv','a+')as f:
        f.write("%s,%s\n"%(y,x))
        f.write("场次,比赛名称,当前场次的排名,当前场次解决的题数,当前场次分数变化,最终的得分,\n")
    get_changshu(url)