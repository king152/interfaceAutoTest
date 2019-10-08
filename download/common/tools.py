# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: tools.py
@creatTime: 2019/09/23
"""

import threading
from download.models import TestSoftId
from download.common.inserts import initPoint, insertDate, initDate, getbate
import random
import string


def getRandom():
    return ''.join(random.sample(string.ascii_letters + string.digits, 6))


# 多线程执行
def runGetid(lock, start, end):
    i = start
    while i < end:
        lock.acquire()
        Soft = TestSoftId.objects.get(id=i)
        Id = Soft.softid
        print(Id)
        initPoint(Id)
        initDate(Id)
        guid = insertDate(Id)
        TestSoftId.objects.filter(id=i).update(guid=guid)
        lock.release()
        i += 1


# 多线程查询结果
def getResult(lock, start, end):
    i = start
    while i < end:
        lock.acquire()
        Soft = TestSoftId.objects.get(id=i)
        Id = Soft.softid
        rd = getbate(str(Id))
        print("资料id为：{}---返利金额：{}".format(Id, rd))
        TestSoftId.objects.filter(id=i).update(result=rd)
        TestSoftId.objects.bulk_update()
        lock.release()
        i += 1


def MyThead(func, startId, endId, step):
    lock = threading.Lock()
    threads = []  # 初始化线程列表
    for i in range(10):
        if i < 9:  # 得到每片最后一个id
            endId = startId + step
        else:  # 最后一片拿到最后一个id
            endId = endId
        print("00")
        t = threading.Thread(target=func, args=(lock, startId, endId,))  # 初始化线程
        threads.append(t)  # 将线程加入threads组
        startId += step  # 得到每片初始id
    for j in threads:  # 开始运行线程
        j.start()
