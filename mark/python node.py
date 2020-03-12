# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import  time
# import requests
# import parsel
# import re
# #谷歌无界浏览器
# from selenium.webdriver.chrome.options import Options
# chrome_options=Options()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_options)
#
# # 打开一个新标签：
# # 我本地用chrome 是正常的，打开了新标签：
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/') #####get' 浏览器没有反应
# time.sleep(2)
# js = "window.open('http://www.sogou.com')"
# driver.execute_script(js)
# time.sleep(5)
#
# #懒加载
# from  selenium import  webdriver
# from urllib.request import urlretrieve
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#     capa = DesiredCapabilities.CHROME
#     capa["pageLoadStrategy"] = "none"  # 懒加载模式，不等待页面加载完毕
#     driver = webdriver.Chrome(desired_capabilities=capa)  # 关键!记得添加
#     wait = WebDriverWait(driver, 5)  # 等待的最大时间20s
#     driver.get(url)
#     wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/div[2]/a[1]')))
#     driver.execute_script("window.stop();")
#
# #下载显示进度条
# def down(url,name):
#     response = requests.get(url,stream = True)
#     zong_size = int(response.headers['content-length'])
#     print('文件大小为：%0.2f MB'% (zong_size/1024/1024))
#     if response.status_code ==200:
#         with open('%s'%name,'wb') as f:
#             start = time.time()
#             size  = 0
#             for data in response.iter_content(chunk_size=1024):
#                 f.write(data)
#                 size+=len(data)
#                 # print(size)
#                 print('\r','下载进度：[','>'*int(100/zong_size*size),'%0.2f'%(size/zong_size*100),'%',']',end='')
#         end = time.time()
#         print('\n','下载用了%0.2f秒'%(end-start))
#     else :
#         print('未响应！！！！')
#
# 邮箱发送：
# from  selenium import webdriver
# import  time
# def youxiang(title,txt):
#     zhuti = '今日故事'
#     #title 是标题
#     #txt 是=正文
#     #发送人
#     out_name=input("输入你要发送的人：")
#     # out_name='1079224933@qq.com'
#     #你自己的账号密码
#     name=("1761512493@qq.com")
#     key = ("lhqlhq1761512493")
#     # driver = webdriver.Chrome()
#     # driver = webdriver.PhantomJS()
#     from selenium.webdriver.chrome.options import Options
#     chrome_options=Options()
#     chrome_options.add_argument('--headless')
#     driver = webdriver.Chrome(chrome_options=chrome_options)
#     url =("https://mail.qq.com/")
#     #
#     #打开浏览器
#     driver.get(url)
#     driver.implicitly_wait(10)
#     #最大化窗口
#     driver.maximize_window()
#     #切换iframe
#     driver.switch_to.frame("login_frame")
#     time.sleep(2)
#
#     ##    # #定位至账号密码登录
#     ##    driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
#     ##    time.sleep(2)
#     ##    #账号，密码输入
#     ##    driver.find_element_by_xpath('//*[@id="u"]').send_keys(name)
#     ##    time.sleep(2)
#     ##    driver.find_element_by_xpath('//*[@id="p"]').send_keys(key)
#     ##    #点击登录
#     ##    driver.find_element_by_xpath('//*[@id="login_button"]').click()
#     ##    点击头像登录
#     driver.find_element_by_xpath('//*[@id="img_out_%s"]'%name[:-7]).click()
#     time.sleep(5)
#     #点击写信
#     driver.find_element_by_xpath('//*[@id="composebtn"]').click()
#     time.sleep(3)
#     #切换iframe至写信
#     driver.switch_to.frame("mainFrame")
#     #driver.switch_to.frame(driver.find_element_by_id('mainFrame'))
#     time.sleep(3)
#     #添加收件人
#     driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys(out_name)
#     #添加主题
#     driver.find_element_by_xpath('//*[@id="subject"]').send_keys(zhuti)
#     #退出当前编辑Iframe
#     driver.switch_to.default_content()
#     #切换Iframe至编辑正文
#     driver.switch_to.frame("mainFrame")
#     #Body_frame=driver.find_element_by_xpath('//iframe[@scrolling="auto"]')
#     Body_frame=driver.find_element_by_class_name("qmEditorIfrmEditArea")
#     driver.switch_to.frame(Body_frame)
#     #添加正文
#     driver.find_element_by_xpath('/html/body').send_keys(title,'\n',txt)
#     time.sleep(3)
#     #退回大Frame再点击发送
#     driver.switch_to.parent_frame()
#     driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
#     time.sleep(5)
#     driver.quit()
#     print("OK")
#
# 中文转编码url
# from urllib import parse
# def utf8_bian_url(name):
#        return parse.quote(name)
#
# #简单GUI
# def tk_GUI(title):
#     import tkinter as tk
#     window = tk.Tk()
#     def hit_me():
#         var.set(status())
#     window .geometry('550x100')
#     l1=tk.Label(window,text = title,font= ('黑体','15'))
#     l1.place(x=0,y=0)
#     var = tk.StringVar()
#     l2 = tk.Label(window,textvariable = var,font = ('黑体','14'))
#     l2.place(x=0,y = 50)
#     e1 = tk.Entry(window,font = ('微软雅黑','15'))
#     e1 .place(x=150,y=0)
#     b1 = tk.Button(window,text = '点击查询',font = ('微软雅黑','15'),command = hit_me)
#     b1.place(x=400,y=0)
#     window.mainloop()
# #键盘监听
# # -*- coding: utf-8 -*-
# """
# Created on Sat Jan 12 14:19:56 2019
# QQ群：476842922(欢迎加群讨论学习)
# @author: Administrator
# """
# import sys, os
# from pynput.keyboard import Controller,Key,Listener
#
# # 监听按压
# def on_press(key):
#     try:
#         print("正在按压:",format(key.char))
#     except AttributeError:
#         print("正在按压:",format(key))
#
# # 监听释放
# def on_release(key):
#     print("已经释放:",format(key))
#
#     if key==Key.esc:
#         # 停止监听
#         return False
#
# # 开始监听
# def start_listen():
#     with Listener(on_press=on_press,on_release=on_release) as listener:
#         listener.join()
#
# if __name__ == '__main__':
#
#     # 实例化键盘
#     kb=Controller()
#
#     # 使用键盘输入一个字母
#     kb.press('a')
#     kb.release('a')
#
#     # 使用键盘输入字符串,注意当前键盘调成英文
#     kb.type("hello world")
#
#     # 使用Key.xxx输入
#     kb.press(Key.space)
#
#     # 开始监听,按esc退出监听
#     start_listen()
# def _wrap_colour(colour, *args):
#     for a in args:
#         print(colour + '{}'.format(a) + '\033[0m')
#
#
# def blue(*args): _wrap_colour('\033[94m', *args)
# def bold(*args): _wrap_colour('\033[1m', *args)
# def cyan(*args): _wrap_colour('\033[96m', *args)
# def darkcyan(*args): _wrap_colour('\033[36m', *args)
# def green(*args): _wrap_colour('\033[92m', *args)
# def purple(*args): _wrap_colour('\033[95m', *args)
# def red(*args): _wrap_colour('\033[91m', *args)
# def underline(*args): _wrap_colour('\033[4m', *args)
# def yellow(*args): _wrap_colour('\033[93m', *args)
#
#
# if __name__ == '__main__':
#     blue('blue')
#     bold('bold')
#     cyan('cyan')
#     darkcyan('darkcyan')
#     green('green')
#     purple('purple')
#     red('r', 'e', 'd')
#     underline('underline')
#     yellow('yellow')
# 彩色打印
# def ppprint(num):
#     x = random.randint(0,7)
#     print("\033[0;3%sm" % x + "%s" % num + "\033[0m")
#
# 词云：
#
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt  #绘制图像的模块
# import  jieba                    #jieba分词
#
# path_txt='C://Users/Administrator/Desktop/all.txt'
# f = open(path_txt,'r',encoding='UTF-8').read()
#
# # 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云
# cut_text = " ".join(jieba.cut(f))
#
# wordcloud = WordCloud(
#    #设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
#    font_path="C:/Windows/Fonts/simfang.ttf",
#    #设置了背景，宽高
#    background_color="white",width=1000,height=880).generate(cut_text)
#
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()
# 图像词云：
#
# from PIL import Image
# from wordcloud import WordCloud, ImageColorGenerator
# import matplotlib.pyplot as plt
# import numpy as np
# import  jieba
# def GetWordCloud():
#    path_txt = 'C://Users/Administrator/Desktop/all.txt'
#    path_img = "C://Users/Administrator/Desktop/timg.jpg"
#    f = open(path_txt, 'r', encoding='UTF-8').read()
#    background_image = np.array(Image.open(path_img))
#    # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云,感兴趣的朋友可以去查一下，有多种分词模式
#    #Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
#    cut_text = " ".join(jieba.cut(f))
#
#    wordcloud = WordCloud(
#        # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
#        font_path="C:/Windows/Fonts/simfang.ttf",
#        background_color="white",
#        # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的
#        mask=background_image).generate(cut_text)
#    # 生成颜色值
#    image_colors = ImageColorGenerator(background_image)
#    # 下面代码表示显示图片
#    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
#    plt.axis("off")
#    plt.show()
#
# if __name__ == '__main__':
#    GetWordCloud()
