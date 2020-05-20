# import requests
# import json
# import time
# import random
# headers = {
# 	'accept-encoding': 'gzip, deflate, br',
# 	'accept-language': 'zh-CN,zh;q=0.9',
# 	'cookie': "INTVER=1; _uuid=243D21F6-1F38-5379-686F-24D0E09DB6D686170infoc; buvid3=30EE56AC-30F8-4047-BD7E-D12F344283A4155819infoc; CURRENT_FNVAL=16; sid=9lbkuy5g; LIVE_BUVID=AUTO1115841951296563; rpdid=|(~|R)~)Rll0J'ul)RumluJ|; DedeUserID=32482364; DedeUserID__ckMd5=ce93b510ef5be598; SESSDATA=9378d768%2C1602042300%2C717d4*41; bili_jct=4e0dc3ac609a998350245370845bde28; bsource=seo_google; bfe_id=1bad38f44e358ca77469025e0405c4a6; PVID=1",
# 	'referer': 'https://space.bilibili.com/32482364/fans/follow',
# 	'sec-fetch-dest': 'script',
# 	'sec-fetch-mode': 'no-cors',
# 	'sec-fetch-site': 'same-site',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
# }

# def followingcount(uid):  #得到mid 的关注的人的个数
# 	url = f'https://api.bilibili.com/x/relation/stat?vmid={uid}'
# 	response = requests.get(url=url, headers=headers)
# 	txt  = json.loads(response.text)
# 	return txt['data']['following']

# def fanscount(uid):  #得到mid 的粉丝的人的个数
# 	url = f'https://api.bilibili.com/x/relation/stat?vmid={uid}'
# 	response = requests.get(url=url, headers=headers)
# 	txt  = json.loads(response.text)
# 	return txt['data']['follower']
# def getfollowing(uid):   #得到mid 的关注的人的信息
# 	fanlist = []
# 	cout = followingcount(uid=uid)
# 	# print(cout)
# 	if(cout%50==0):
# 		pages = cout//50
# 	else :
# 		pages = cout//50 +1
# 	for i in range(1,pages+1):
# 		# print(i)
# 		if(i>=6):
# 			break
# 		url = f"https://api.bilibili.com/x/relation/followings?vmid={uid}&pn={i}&ps=50&order=desc&jsonp=jsonp&callback=__jp11"
# 		r = requests.get(url =url,headers = headers)
# 		r = r.text[7:][:-1]
# 		txt = json.loads(r)
# 		lists = txt['data']['list']
# 		# print(len(lists))
# 		for x in lists:
# 			# print(x['uname'],": ",x['mid'])
# 			fanlist.append(str(x['mid'])+"-"+str(x['uname']))
# 	return fanlist
# def dailichi():
# 	import random
# 	daili = [
# 		'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
# 		'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; WOW64; Trident/4.0; SLCC1)',
# 		'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)',
# 		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
# 		'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
# 		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71',
# 		'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
# 		'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
# 		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
# 	]
# 	dai = random.choice(daili)
# 	# print(dai)
# 	head  ={
# 		'User-Agent':'%s'% dai
# 	}
# 	return head

# def getfans(uid):   #得到mid 的粉丝的人的信息
# 	fanlist = []
# 	cout = fanscount(uid=uid)
# 	if(cout%50==0):
# 		pages = cout/50
# 	else :
# 		pages = cout//50 +1
# 	print(pages)
# 	for i in range(1,pages+1):

# 		url = f"https://api.bilibili.com/x/relation/followers?vmid={uid}&pn={i}&ps=50&order=desc&jsonp=jsonp&callback=__jp10"
# 		r = requests.get(url =url,headers = headers)
# 		r = r.text[7:][:-1]
# 		txt = json.loads(r)
# 		lists = txt['data']['list']
# 		# print(len(lists))
# 		for x in lists:
# 			# print(x['uname'],": ",x['mid'])
# 			fanlist.append(str(x['mid'])+"-"+str(x['uname']))
# 	return fanlist

# def main():
# 	fans = getfans(32482364)
# 	print(fans)
# 	# print(len(fans))
# 	dictt = {}
# 	for x in fans:
# 		mid = x.split('-')[0]
# 		print(x.split('-')[1]," :: ")
# 		l = getfollowing(mid)
# 		print(l)
# 		for i in l:
# 			# with open("a.csv",'a+','utf-8')as f:
# 			# 	f.write(str(i)+'\n')
# 			word = i.split('-')[0]
# 			if word in dictt:
# 				dictt[word] += 1
# 			else:
# 				dictt[word] = 1

# 		timee = random.randint(1,5)
# 		time.sleep(timee)
# 	print(dictt)
# import re 
# def get_name(id):
#     url =f'https://space.bilibili.com/{id}'
#     response = requests.get(url=url,headers=dailichi())
#     txt = response.text
#     name = re.findall('<title>(.*?)的个人空间 - 哔哩哔哩',txt,re.S)[0]
#     return name



# items = [('9824766', 108),
# 		('26366366', 111),
# 		('546195', 118),
# 		('777536', 118),
# 		('20165629', 120),
# 		('456664753', 121),
# 		('353840826', 130),
# 		('517327498', 162),
# 		('326499679', 165),
# 		('14110780', 174)]
# for x in items:
# 	print(x[0],get_name(x[0]),":",x[1])
print("111")