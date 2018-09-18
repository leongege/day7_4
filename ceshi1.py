#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
import sys
# x = input("请输入要备份的源文件")
# y = input("请输入备份的目标文件")
# 使用方法 python ceshi1.py  源文件  目标文件
#传两个参数
x = sys.argv[1]
y = sys.argv[2]
#打开源文件，只读
#打开目标文件，追加模式
f1 = open(x,"r")
f2 = open(y,"a")
while True:
    #读取源文件数据
    data = f1.read()
    if not data:
        break
    #把数据写入f2中
    f2.write(data)
#关闭打开的文件
f1.close()
f2.close()