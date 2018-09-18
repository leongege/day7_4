#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"

class Meat(object):
    def __init__(self):
        self.name = "肉"
        self.weight = 2
class Ham(Meat):
    #pass
    def __init__(self):
        super().__init__()
        self.name = "火腿"
class Persion:
    def eat(self,obj):
        print("他喜欢吃%s" %obj.name)
rou = Meat()
huo = Ham()
obj = Persion()
obj.eat(huo)