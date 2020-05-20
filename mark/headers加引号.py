import re
headers_str = """
Referer: https://github.com/ngosang/trackerslist
Sec-Fetch-Dest: document
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36
"""
pattern = '^(.*?): (.*)$'
print('headers = {',end='')
for line  in headers_str.splitlines():
    print("\t",end='')
    print(re.sub(pattern,'\'\\1\': \'\\2\',',line))
print("}")