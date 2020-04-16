#!/usr/bin/python3",
# -*- encoding: utf-8 -*-",
'''
@File    :   req.py
@Time    :   2020/3/15  20:23:23
@Author  :   *华强
@Contact :   1761512493@qq.com
'''
def get_cook():
    import re
    with open('cook.txt') as f:
        txt = f.read()
    headers_str = f"{txt}"
    pattern = '^(.*?): (.*)$'
    cook = ('{\n')
    for line  in headers_str.splitlines():
        cook+=("\t")
        cook+=(re.sub(pattern,'\'\\1\': \'\\2\',',line))
        cook+="\n"
    cook+=("}")
    cook = eval(cook)
    return cook
def get_from_data():
    import re
    with open('from_data.txt') as f:
        txt = f.read()
    headers_str = f"{txt}"
    pattern = '^(.*?): (.*)$'
    from_data = ('{\n')
    for line  in headers_str.splitlines():
        from_data+=("\t")
        from_data+=(re.sub(pattern,'\'\\1\': \'\\2\',',line))
        from_data+="\n"
    from_data+=("}")
    from_data = eval(from_data)
    return from_data

def get_url():
    with open('url.txt') as f:
        url = f.read()
    return  url

import requests
if (get_cook()=={} and get_from_data()=={}):
    print(1)
    response = requests.get(url=get_url())
elif (get_from_data()=={}):
    print(2)
    response = requests.get(url=get_url(),headers = get_cook())
else :
    print(3)
    response = requests.post(url=get_url(),headers = get_cook(),data = get_from_data())
response.encoding = response.apparent_encoding
print(response.text)