# import requests
# def panduan(ip):
#     url = "http://httpbin.org/get"
#     headers = {
#         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
#         }
#     proxies = {
#         'http':str(ip[0])+":"+str(ip[1]),
#         'https':str(ip[0])+":"+str(ip[1]),
#     }
#     try:
#         response = requests.request("GET", url, headers=headers, proxies=proxies, timeout=5)
#         if response.status_code==200:
#             panduan = response.json()['origin'].split(",")[0]
#             if panduan!=None:
#                 return True
#             else :
#                 return False
#         else:
#             return False
#     except:
#         return False
# print(panduan(["115.221.245.229","9999"]))
