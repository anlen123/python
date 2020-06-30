#%%
import requests
import re 
import parsel
import time
with open("房价.csv","a+")as f:
 	f.write("地段,室,厅,名字,朝向,精装还是简装,挂牌价,成交价,价格,建房时间,成交周期"+"\n")
url = "https://cd.lianjia.com/chengjiao/"
for url_num in range(1,2):
	url = f"https://cd.lianjia.com/chengjiao/pg{url_num}/"
	print(url)
	headers = {	
		'Connection': 'keep-alive',
		'Cookie': 'lianjia_uuid=5eb3fa52-cf2c-4eac-9fc4-78e0c57c8bff; select_city=510100; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172b216ea99629-0fbf14c26115d5-3f6b4b05-2073600-172b216ea9a439%22%2C%22%24device_id%22%3A%22172b216ea99629-0fbf14c26115d5-3f6b4b05-2073600-172b216ea9a439%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; lianjia_ssid=009be2ad-feee-40cd-b778-20f10cd0d63e; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiODYyMWFlZjlkOWZkMWE4YzhmMWUxYjM3OWIzZWExNjI3N2ZmMWUyOTI1ODhkNTNjMzI5NzY1NzU3NGYzZTk4ODIzMmNlZjgzYjQ5NWI1MDBjNzBjOTEzMTVlYTA1ZGI4ZTJiMWY0MGU0OGFmZmVjNTljMmU0Mjg4NDBjYzZkNWZhYmUyMmE2NDE1ZjYyOWM5MWI0MTBiNzgyYzU5MmE5OGZkOTYxMGMwMDQzZmRjZjFlYjZhY2Y0ZTYwZmEwMDFhOGE1YWJhNDE4NWU3NTljMjEzNjY0MTM1Mzc4OWEyMjI3M2YzMDI0MzUxZTE0YTJkMzU0NDA3MzBlZDMxYTFmZGY0ZjVhYjEyMWQ4NTZiZTNkMDdjYzZmYTdlM2UyYWQ4N2FkNmRhMDM4YmJjNmMwYTlkOGQ1MDRlZGVkNGU0YWZjOGMzYjU3ODYxNGQ4ZDYwM2I3MGI4MjQ5ZjYzY2M1NlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJjOWUyYTIxZlwifSIsInIiOiJodHRwczovL2NkLmxpYW5qaWEuY29tL2NoZW5namlhby8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
		'Host': 'cd.lianjia.com',
		'Referer': 'https://cd.lianjia.com/chengjiao/pg3/',
		'Sec-Fetch-Dest': 'document',
		'Sec-Fetch-Mode': 'navigate',
		'Sec-Fetch-Site': 'same-origin',
		'Sec-Fetch-User': '?1',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
	}

	r = requests.get(url = url,headers = headers)
	# print(r.text)

	sel = parsel.Selector(r.text)

# %%
名字集合 = sel.xpath(f'/html/body/div[5]/div[1]/ul/li[1]').re('<a href=".*?"_blank">(.*?)</a>')[0]
# print(名字集合)
名字集合 = str(名字集合).split(" ")
名字 = 名字集合[0]
print(名字)

面积= 名字集合[2]
print(面积)

室 = re.findall("(\d)室\d厅",名字集合[1])[0]
print(室)
厅= re.findall("\d室(\d)厅",名字集合[1])[0]
print(厅)
# %%
