#!/usr/bin/python
# -*- coding: UTF-8 -*-

import platform


# 获取当前的操作系统类型
def get_current_platform():
    if platform.system() == 'Windows':
        print('Windows系统')
        return 1
    elif platform.system() == 'Linux':
        print('Linux系统')
        return 2
    elif platform.system() == 'Darwin':
        print('Mac OS系统')
        return 3
    raise Exception('unsupported other operating system')
