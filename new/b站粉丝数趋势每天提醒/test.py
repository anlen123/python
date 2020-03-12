import requests
import os 
import re
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
    # print(dai)
    head  ={
        'User-Agent':'%s'% dai
    }
    return head
def get_name(id):
    url =f'https://space.bilibili.com/{id}'
    response = requests.get(url=url,headers=dailichi())
    txt = response.text
    name = re.findall('<title>(.*?)的个人空间 - 哔哩哔哩',txt,re.S)[0]
    return name
def main(id):
    url = f'https://api.bilibili.com/x/relation/stat?vmid={id}'
    name = get_name(id)
    timee = get_time()
    response = requests.get(url=url,headers=dailichi())
    pep = response.json()['data']['follower']
    # print(response.json()['data']['follower'])
    with open(f'{name}粉丝数.txt','a+')as f:
        f.write(str(timee)+','+str(pep)+'\n')
    file = open(f'{name}粉丝数.txt')
    txt =''
    x= file.read().split('\n')
    if len(x)==2:
        txt+=f'{name},你昨天的粉丝我不知道耶\n'
    else :
        txt+=f"{name},你昨天的粉丝是：{x[-3].split(',')[1]}\n"
    txt+=f'{name},你今天的粉丝是：{pep}\n'
    file.close()
    if len(x)==2:
        txt+='对不起，我求不到差值耶！！'
    else :
        cha = int(pep)-int(x[-3].split(',')[1])
        if cha==0:
            txt+=f'{name},今天你的粉丝量没变哦还是{pep}!!!!，加油做新视频哦！'
        elif cha>0:
            txt+=f'{name},今天你的粉丝涨了{cha}个,加油啊，可真的是一个优秀的up主呢!!'
        else :
            txt+=f'{name},今天你的粉丝减了{cha}个,是不是又在当鸽子了，赶快去更视频吧！！'
    return txt
def qq_youjian(fajianren,shoujianren,zhuti,txt):
    import smtplib
    from email.mime.text import MIMEText
    msg_from=fajianren                            #发送方邮箱
    # passwd='eyfdfamsmdsldchg'                                   #填入发送方邮箱的授权码
    passwd='fcznjllwfnqcdbca'                         #填入发送方邮箱的授权码
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


def get_time():
    import datetime
    now_time = str(datetime.datetime.now())[:10]
    return now_time
get_time()
if __name__ == "__main__":
    # print(main('32482364'))
    qq_youjian('1761512493@qq.com','1761512493@qq.com','你的今日粉丝趋势', main('32482364'))
    qq_youjian('1761512493@qq.com','1477388008@qq.com','你的今日粉丝趋势', main('259551152'))