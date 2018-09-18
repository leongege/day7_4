#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"

import os
import sys
x = sys.argv[1]
if os.path.isdir(x):
    os.makedirs(x)
else:
    os.mknod(x)
