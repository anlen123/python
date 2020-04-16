import re
headers_str = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: __cfduid=d706a4bab57a90f84beab61c9ed006a1f1584276309; yjs_id=fDE1ODQyNzYzMTMwMTE; ctrl_time=1; watch_times=0
Host: acg17.com
If-Modified-Since: Sun, 15 Mar 2020 10:15:13 GMT
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
"""
pattern = '^(.*?): (.*)$'
print('headers = {',end='')
for line  in headers_str.splitlines():
    print("\t",end='')
    print(re.sub(pattern,'\'\\1\': \'\\2\',',line))
print("}")