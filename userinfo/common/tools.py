# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: tools.py
@creatTime: 2019/09/19
"""

import base64
import random
import string


# 加密
def encrypt(strings):
    return ''.join(random.sample(string.ascii_letters + string.digits, 8)) + \
           (base64.b64encode(strings.encode(encoding="utf-8"))).decode() + \
           ''.join(random.sample(string.ascii_letters + string.digits, 6))


# 解密
def decrypt(strings):
    return (base64.b64decode(strings[8:][:-6])).decode()
