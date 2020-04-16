# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  刘华强
@Version        :  
------------------------------------
@File           :  文件批量重命名.py
@Description    :  
@CreateTime     :  2019/11/27 17:45
------------------------------------
@ModifyTime     :  
"""
import pyautogui,sys,time
import cv2
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import random
from ctypes import *  # 获取屏幕上某个坐标的颜色
def dianji(x,y):    
    pyautogui.click(x,y, clicks=1,button='left')
def get_color(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return [r, g, b]

def get_juping():
    hwnd_title = dict()
    def get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t is not "":
            # print(h, t)
            if t =="阴阳师-网易游戏":
                return h

def get_img(xx):
    hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(xx).toImage()
    img.save("a.jpg")
def img_pipei1(b):
    #opencv模板匹配----单目标匹配
    #读取目标图片
    target = cv2.imread("a.jpg")
    #读取模板图片
    template = cv2.imread(b)
    #获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
    #归一化处理
    cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    #寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    gao,kuan = target.shape[:2]
    xx = (min_loc[0]+twidth/2)/kuan
    yy = (min_loc[1]+theight/2)/gao
    #匹配值转换为字符串
    #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    #对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    # strmin_val = str(min_val)
    # #绘制矩形边框，将匹配区域标注出来
    # #min_loc：矩形定点
    # #(min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    # #(0,0,225)：矩形的边框颜色；2：矩形边框宽度
    # cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
    # #显示结果,并将匹配值显示在标题栏上
    # cv2.imshow("MatchResult----MatchingValue="+strmin_val,target)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    # print(min_val)
    if abs(min_val)<=2.0e-10:
        print("YES")
        dianji(1135 * xx, yy * 671)
    else :
        print("NO")
        dianji(1047, 478)
def img_pipei(b):
    #opencv模板匹配----单目标匹配
    #读取目标图片
    target = cv2.imread("a.jpg")
    #读取模板图片
    template = cv2.imread(b)
    #获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
    #归一化处理
    cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    #寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    gao,kuan = target.shape[:2]
    xx = (min_loc[0]+twidth/2)/kuan
    yy = (min_loc[1]+theight/2)/gao
    #匹配值转换为字符串
    #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    #对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    # strmin_val = str(min_val)
    # #绘制矩形边框，将匹配区域标注出来
    # #min_loc：矩形定点
    # #(min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    # #(0,0,225)：矩形的边框颜色；2：矩形边框宽度
    # cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
    # #显示结果,并将匹配值显示在标题栏上
    # cv2.imshow("MatchResult----MatchingValue="+strmin_val,target)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    # print(min_val)
    if abs(min_val)<=2.0e-10:
        print("YES")
        dianji(1135 * xx, yy * 671)
def img_pipei2(b):
    #opencv模板匹配----单目标匹配
    #读取目标图片
    target = cv2.imread("a.jpg")
    #读取模板图片
    template = cv2.imread(b)
    #获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
    #归一化处理
    cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    #寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    gao,kuan = target.shape[:2]
    xx = (min_loc[0]+twidth/2)/kuan
    yy = (min_loc[1]+theight/2)/gao
    #匹配值转换为字符串
    #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    #对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    # strmin_val = str(min_val)
    # #绘制矩形边框，将匹配区域标注出来
    # #min_loc：矩形定点
    # #(min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    # #(0,0,225)：矩形的边框颜色；2：矩形边框宽度
    # cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
    # #显示结果,并将匹配值显示在标题栏上
    # cv2.imshow("MatchResult----MatchingValue="+strmin_val,target)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    # print(min_val)
    if abs(min_val)<=9e-10:
        print("YES")
        dianji(1135 * xx, yy * 671)
    else :
        dianji(622,447)
id = get_juping()
while True:
    get_img(id)
    img_pipei('tan.jpg')
    time.sleep(2)
    img_pipei2('zhan.jpg')
    time.sleep(2)
    img_pipei('KO.jpg')
    time.sleep(2)