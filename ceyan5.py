#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"

import string
import random
#导入两个函数
#大小写字母 数字 全部包含
all_choice = string.ascii_letters + string.digits
def pass1(num = 8):#循环8次
    pwd = ""
    for i in range(num):
        pwd  += random.choice(all_choice)#随机选一个  字符拼接
    return pwd
if __name__ == "__main__":
    print(pass1(8))