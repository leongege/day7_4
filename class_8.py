#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
class Dog:
    def __init__(self,names):
        self.name = names
    def __str__(self):
        return "name is %s "  %self.name
dog1 = Dog("heihei")
print(dog1)