import re
headers_str = """
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8
cache-control: max-age=0
cookie: l=v; CURRENT_FNVAL=16; rpdid=|(u|kJJYJ)kk0J'ul)m|||J~R; DedeUserID=32482364; DedeUserID__ckMd5=ce93b510ef5be598; SESSDATA=d18c7191%2C1604805447%2C079d9*51; bili_jct=ef9f538472e653e7704e8891a7473c78; LIVE_BUVID=AUTO8515892534539478; sid=jaqm2ir8; _uuid=D2FA917B-A38C-8717-DAAC-D9393033FDE408502infoc; deviceFingerprint=0a4bb09422c47d2cfaec122043be504c; msource=ad_10023056xx_cpc_3; kfcSource=ad_10023056xx_cpc_3; buvid3=C916FB30-EC6F-41DD-9451-10D97F3CB647155817infoc; PVID=2; CURRENT_QUALITY=112; bsource=share_source_copy_link; bp_video_offset_32482364=410343662246463157; bp_t_offset_32482364=410344714520799238
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36
"""
pattern = '^(.*?): (.*)$'
print('headers = {',end='')
for line  in headers_str.splitlines():
    print("\t",end='')
    print(re.sub(pattern,'\'\\1\': \'\\2\',',line))
print("}")


