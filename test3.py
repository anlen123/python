# -*- coding: utf-8 -*-
#!/usr/bin/python3
'''
B站粉丝监控，消息发送
@File    :   test2.py
@Time    :   2020/07/11
@Author  :   未闻丶死讯
@Contact :   1761512493@qq.com
'''
import requests
import re
import time
import os
import random
from fake_useragent import UserAgent

ua = UserAgent()
have = []
# 你的b站cookies 不知道怎么获取自己百度

cook = "sid=iltqdyjb; DedeUserID=32482364; DedeUserID__ckMd5=ce93b510ef5be598; SESSDATA=8a59ae8e%2C1604628849%2Cddb89*51; bili_jct=3fda1881cb2b6d0fae6908d3cb614ad0; CURRENT_FNVAL=16; rpdid=|(u|kJJYJ~lY0J'ul)m|~YmJ|; LIVE_BUVID=AUTO8615892797682858"
uid = re.findall("DedeUserID=(.*?);", cook)[0]
csrf = re.findall("bili_jct=(.*?);", cook)[0]


def BV_AV(BV):
    table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
    tr = {}
    for i in range(58):
        tr[table[i]] = i
    s = [11, 10, 3, 8, 4, 6]
    xor = 177451812
    add = 8728348608
    r = 0
    for i in range(6):
        r += tr[BV[s[i]]] * 58 ** i
    return (r - add) ^ xor


def _Send(BV, msg):
    url = "https://api.bilibili.com/x/v2/reply/add"

    aid = BV_AV(BV)

    data = {
        'oid': f'{aid}',
        'type': '1',
        'message': f'{msg}',
        'plat': '1',
        'jsonp': 'jsonp',
        'csrf': f'{csrf}',
    }
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'content-length': '114',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': f"{cook}",
        'origin': 'https://www.bilibili.com',
        'referer': f'https://www.bilibili.com/video/{BV}',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': ua.random,
    }

    session = requests.Session()
    if session.post(url=url, data=data, headers=headers).status_code == 200:
        print(BV + "已评论")
    else:
        print(BV + "false!!")


def get_BV_list():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': f"{cook}",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua.random,
    }
    a = requests.get(
        # url="https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid=32482364&type_list=268435455",
        url=f"https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid={uid}&type_list=8",
        headers=headers).text
    return re.findall('"bvid":"(.*?)"', a)[:5]


def save_have():
    global have
    if have:
        with open("hava.txt", "w+") as f:
            for x in have:
                f.write(str(x) + "\n")

    if os.path.exists("hava.txt"):
        with open("hava.txt", "r") as f:
            have = f.read().split("\n")[:-1]


def main():
    global have
    i = 0
    while True:
        i += 1
        BV_list = get_BV_list()
        for x in BV_list:
            if x not in have:
                _Send(x, "我来啦,")
                have.append(x)
        if i == (3600 / 5):
            i = 0
            save_have()
        time.sleep(random.randint(3, 5))


if __name__ == '__main__':
    # main()
    _Send("BV1Mk4y1B7b8", "来了")
