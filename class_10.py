#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
class A():
    name = "tom"
    age = 21
    def work(self):
        print("敲代码")

class B(A):
    name = "jim"
    def work(self):
        print("lifa")

class C(B):
    pass

# jack = A()
# print(jack.name)


# jack = B()
# jack.work()
# print(jack.name,jack.age)


# tom = C()
# print(tom.name,tom.age)
# tom.work()


tom = C()
print(C.__mro__)
print(B.__mro__)