#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   Test_01.py
@Time    :   2020/03/15 12:08:58
@Author  :   *华强
@Contact :   1761512493@qq.com
'''

import random
class Dog ():
    dog_list=[]

    @classmethod
    def num_dog(cls):
        return len(Dog.dog_list)

    @staticmethod
    def intrduce():
        print("dog is human's best friend!!")

    def __init__(self,name,height,power):
        self.name = name
        self.height = height
        self.power = power
        self.bool = 100
        # self._xxx= _xxx     前面_表示私有
        Dog.dog_list.append(self)
        print(f"我是{self.name},我出生了,汪汪汪!!!")

    def bark(self):
        print(f"我叫{self.name},我的身高是{self.height},攻击力为{self.power},当前血量{self.bool}")

    def attack(self,dog2):
        bao_attack = random.randint(1,10)
        print(f"{self.name}攻击了{dog2.name}")
        if (bao_attack==5):
            dog2.reduce_bool(self.power*2)
            print(f"{self.name}会心一击!")
            print(f"{dog2.name}受到了{self.power*2}的伤害!")
        else :
            dog2.reduce_bool(self.power)
            print(f"{dog2.name}受到了{self.power}的伤害!")
    def reduce_bool(self,power_value):
        self.bool-=power_value

class DogSheep(Dog):
    def __init__(self, name, height, power,sheep_num):
        super().__init__(name, height, power)
        self.sheep_num = sheep_num
    
    def Sheep_Work(self):
        print(f"{self.name},开始保护羊了")
    def bark(self):
        print(f"我是牧羊犬{self.name},我骄傲!")
        super().bark()
