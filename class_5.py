#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
class Calucation:
    """Usage:class"""
    def __init__(self,passx,passy):
        """Usage:init"""
        self.x = passx
        self.y = passy
        # self.he = 0
        # self.cha = 0

    def sum(self):
        """Usage:sum"""
        return "%s + %s = %s" %(self.x,self.y,self.x + self.y)
    def  suba(self):
        """Usage:suba"""
        return "%s - %s = %s" %(self.x,self.y,self.x - self.y)

if __name__ ==  "__main__":
    one = Calucation(10,5)
    print(one.sum())
    print(one.suba())