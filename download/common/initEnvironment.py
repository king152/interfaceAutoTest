# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: initEnvironment.py
@creatTime: 2019/09/20
"""

from download.common.insertSql import getSoftid
from download.models import SoftId, TestCase
from Logs.log import get_log

log = get_log("initEnvironment")


# softID查重
def rechecking(soft):
    try:
        count = TestCase.objects.filter(softId=soft)
    except Exception as e:
        log.info("登录用户查询异常：", e)
        count = None
    return count


# 初始化环境
def initEnviron():
    data = getSoftid(100000)
    soft_list = []
    for d in data:
        soft_list.append(SoftId(softId=d[0]))
    SoftId.objects.bulk_create(soft_list)
