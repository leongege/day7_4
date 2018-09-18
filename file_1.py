#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
# import os,sys
# from random import choice
# l = [1,2,3,4]
# print(choice(l))

#第一种引用
# import a.mod2
# print(a.mod2.fun2(2,3))

#第二种引用
from a.mod2 import fun2
print(fun2(4,5))

