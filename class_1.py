#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
class Student():
    def work(self):
        print("aaa")
    def eat(self):
        print("bbb")

tom = Student()

#首次赋值，定义属性
tom.id = "1001"
tom.address = "BJ"
print(tom.id)
print("tom id :  %s  tom jia shi %s" %(tom.id,tom.address))


jack = Student()
jack.id = "1002"
jack.address = "NJ"
print("jack id :  %s  jack jia shi %s" %(jack.id,jack.address))