import re
headers_str = """
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 255
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: JSESSIONID=85f3350bfe51bdbc99f77e18e510; watch_times=0; JSESSIONID=85f3350bfe51bdbc99f77e18e510; insert_cookie=67313298
Host: deal.ggzy.gov.cn
Origin: https://deal.ggzy.gov.cn
Referer: https://deal.ggzy.gov.cn/ds/deal/dealList.jsp
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
X-Requested-With: XMLHttpRequest
"""
pattern = '^(.*?): (.*)$'
print('headers = {',end='')
for line  in headers_str.splitlines():
    print("\t",end='')
    print(re.sub(pattern,'\'\\1\': \'\\2\',',line))
print("}")