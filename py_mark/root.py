import requests
import time
#下载快的
def download_img(url,name):
    from  urllib.request import urlretrieve
    urlretrieve(url,'./%s.jpg'%name)

#保存进文件txt
def download_txt(filename, contents):
    fh = open(filename, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()
#保存图片
def get_img(url,name):
    path = './%s.jpg'%name
    r = requests.get(url)
    with open(path, 'wb') as f:
        f.write(r.content)
#下载音乐和视频
def download_music(url,name):
    from urllib import request
    path = './%s.mp3'%name
    request.urlretrieve(url, path)
    print('下载完成')
#下载显示进度条
def download_jindu(url,name):
    response = requests.get(url,stream = True)
    zong_size = int(response.headers['content-length'])
    print('文件大小为：%0.2f MB'% (zong_size/1024/1024))
    if response.status_code ==200:
        with open('%s'%name,'wb') as f:
            start = time.time()
            size  = 0
            for data in response.iter_content(chunk_size=1024):
                f.write(data)
                size+=len(data)
                # print(size)
                print('\r','下载进度：[','>'*int(100/zong_size*size),'%0.2f'%(size/zong_size*100),'%',']',end='')
        end = time.time()
        print('\n','下载用了%0.2f秒'%(end-start))
    else :
        print('未响应！！！！')
def get_page(url):
    reponse = requests.get(url,headers = dailichi())
    reponse.encoding="UTF-8"
    text = reponse.text
    print(text)
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
    print(dai)
    head  ={
        'User-Agent':'%s'% dai
    }
    return head
def tihuan(ss):
    return  ss.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','').replace('.','')
def qq_youjian(fajianren,shoujianren,zhuti,txt):
    import smtplib
    from email.mime.text import MIMEText
    msg_from=fajianren                                 #发送方邮箱
    # passwd='eyfdfamsmdsldchg'                                   #填入发送方邮箱的授权码
    passwd='eyfdfamsmdsldchg'                         #填入发送方邮箱的授权码
    msg_to=shoujianren                                       #收件人邮箱

    subject=zhuti                                   #主题
    content=txt #正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com",465) #邮件服务器及端口号
        s.login(msg_from, passwd)                               #登录SMTP服务器
        s.sendmail(msg_from, msg_to, msg.as_string())#发邮件 as_string()把MIMEText对象变成str
        print ("发送成功")
    except s.SMTPException:
        print ("发送失败")
    finally:
        s.quit()
def guge_wutu():
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    #1允许所有图片；2阻止所有图片；3阻止第三方服务器图片
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2
        }
    }
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=options)
    # driver.get("http://huaban.com/")
    #driver.quit()
    return driver
def wujie_wutu():
    from selenium import webdriver
    SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
    di = webdriver.PhantomJS(service_args=SERVICE_ARGS)
    return di
# def guge_lanjiazai():
#     #懒加载
#     from  selenium import  webdriver
#     from urllib.request import urlretrieve
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#     from selenium.webdriver.support import expected_conditions as EC
#     from selenium.webdriver.common.by import By
#     capa = DesiredCapabilities.CHROME
#     capa["pageLoadStrategy"] = "none"  # 懒加载模式，不等待页面加载完毕
#     driver = webdriver.Chrome(desired_capabilities=capa)  # 关键!记得添加
#     wait = WebDriverWait(driver, 5)  # 等待的最大时间20s
#     driver.get(url)
#     wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/div[2]/a[1]')))
#     driver.execute_script("window.stop();")
def IDM_DOWN(url,Down_Path,OutPutFileName="",mode='wait'):
    # """
    # /d URL - 下载一个文件，等等
    # /s - 开始任务调度里的队列
    # /p 本地_路径 - 定义要保存的文件放在哪个本地路径
    # /f 本地local_文件_名 - 定义要保存的文件到本地的文件名
    # /q - IDM 将在成功下载之后退出。这个参数只为第一个副本工作
    # /h - IDM 将在成功下载之后挂起您的连接
    # /n - 当不要 IDM 询问任何问题时启用安静模式
    # /a - 添加一个指定的文件 用 /d 到下载队列，但是不要开始下载
    # """
    from subprocess import call
    IDM = r'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'
    if mode == "wait":
        call([IDM, '/d',url, '/p',Down_Path, '/f', OutPutFileName, '/n','/a','/q'])
    elif mode=="down":
        call([IDM, '/d',url, '/p',Down_Path, '/f', OutPutFileName, '/n','/q','/h'])
def IDM_MAIN():
    from subprocess import call
    IDM = r'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'
    call([IDM, '/s'])
def panduan_ip(ip): # panduan_ip(["115.221.245.229","9999"])
    url = "http://httpbin.org/get"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        }
    proxies = {
        'http':str(ip[0])+":"+str(ip[1]),
        'https':str(ip[0])+":"+str(ip[1]),
    }
    try:
        response = requests.request("GET", url, headers=headers, proxies=proxies, timeout=5)
        if response.status_code==200:
            panduan = response.json()['origin'].split(",")[0]
            if panduan!=None:
                return True
            else :
                return False
        else:
            return False
    except:
        return False

