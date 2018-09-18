#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"

class Dog:
    def __init__(self,names,legs,ages,colors):
        self.name = names
        self.leg = legs
        self.age = ages
        self.color = colors
    def show(self):
        return "名字：%s ，腿：%s ，年龄：%s，颜色：%s"  %(self.name,self.leg,self.age,self.color)


dog1 = Dog("花花","4","5","B")
print("first dog " + dog1.show())

dog2 = Dog("wangwang","2","3","W")
dog2.show()