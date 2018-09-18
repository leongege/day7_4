#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"

class Dog:
    def __init__(self):
        self.name = "花花"
        self.leg = 4
        self.age = 3
        self.color = "B"
    def show(self):
        print("名字：%s ，腿：%s ，年龄：%s，颜色：%s"  %(self.name,self.leg,self.age,self.color))


dog1 = Dog()
dog1.show()

dog2 = Dog()
dog2.show()