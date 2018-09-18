#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
class Dog:
    def __del__(self):
        print("塔被干掉了")

lh = Dog()
print(lh)
print("*" * 20)