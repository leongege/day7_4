#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"

class F():
    def s(self):
        print("sing")
    def eat(self):
        print("eat apple")
class M():
    def d(self):
        print("dance")
    def eat(self):
        print("eat orange")

# class C(F,M):
#     pass


class C(F,M):
    def eat(self):
        F.eat()


tom = C()
tom.s()
tom.d()
tom.eat()
