#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
import sys
prompt = """1 前进
2左转
3右转
4退出
请在（1/2/3/4）中选择
"""
while True:
    print(prompt)
    x = int(input("输入选择的数字"))
    if x == 4:
        sys.exit()