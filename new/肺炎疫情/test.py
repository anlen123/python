#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   文件批量重命名.py
@Time    :   2020/02/11 18:49:24
@Author  :   刘华强
@Contact :   1761512493@qq.com
'''
import requests
import os 
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

def 获取全国的总数据():
    url = 'http://www.dzyong.top:3005/yiqing/total'
    data = requests.get(url=url,headers=dailichi()).json()
    确诊=data['data'][0]['diagnosed']
    疑似=data['data'][0]['suspect']
    死亡=data['data'][0]['death']
    治愈=data['data'][0]['cured']
    return "确诊:"+str(确诊)+'\n疑似:'+str(疑似)+'\n死亡:'+str(死亡)+'\n治愈:'+str(治愈)

def 获取历史数据():
    url ='http://www.dzyong.top:3005/yiqing/history'
    data = requests.get(url=url,headers=dailichi()).json()['data']
    # txt = []
    if os.path.exists("%s.csv"%(data[0]['date'])):
        os.remove("%s.csv"%(data[0]['date']))
    with open('%s.csv'%(data[0]['date']),'a+')as f:
        f.write('时间,确诊人数,疑似人数,治愈人数,死亡人数,疑似人数增量\n')

    for x in data[::-1]:
        # txt+=('时间:'+str(x['date']),'确诊人数:'+str(x['confirmedNum']),'疑似人数:'+str(x['suspectedNum']),'治愈人数:'+str(x['curesNum']),'死亡人数:'+str(x['deathsNum']),'疑似人数增量:'+str(x['suspectedIncr']))
        with open('%s.csv'%(data[0]['date']),'a+')as f:
            f.write(str(x['date'])+','+str(x['confirmedNum'])+','+str(x['suspectedNum'])+','+str(x['curesNum'])+','+str(x['deathsNum'])+','+str(x['suspectedIncr'])+'\n')

def 获取疫情数据地区():
    url ='http://www.dzyong.top:3005/yiqing/area'
    data = requests.get(url=url,headers=dailichi()).json()['data']
    if os.path.exists("地区疫情情况.csv"):
        os.remove('地区疫情情况.csv')
    with open('地区疫情情况.csv','a+')as f:
        f.write('省,城市,确证人数,疑似人数,治愈人数,死亡人数\n')
    for x in data:
        # print(x['provinceName'],x['cityName'],x['confirmedCount'],x['suspectedCount'],x['curedCount'],x['deadCount'])
        with open('地区疫情情况.csv','a+')as f:
            f.write(str(x['provinceName'])+','+str(x['cityName'])+','+str(x['confirmedCount'])+','+str(x['suspectedCount'])+','+str(x['curedCount'])+','+str(x['deadCount'])+'\n')
