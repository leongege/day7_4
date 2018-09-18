#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"

class Persion:
    def introduce(self):
        print("名字是： %s , age :  %s ,家庭住址 %s"  %(self.name,self.age,self.address))

tom = Persion()
tom.name = "tom"
tom.age = "16"
tom.address = "Bj"

tom.introduce()