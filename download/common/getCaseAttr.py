# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: getCaseAttr.py
@creatTime: 2019/09/26
"""

import random
import datetime
import time


def isDate(date):
    try:
        if ":" in date:
            datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        elif "-" in date:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        else:
            datetime.datetime.strptime(date, "%Y%m%d")
        return True
    except Exception as e:
        print(e)
        return False


# 根据ID返回相应名称
def getDownloadAuthorType(downloadId):
    if downloadId == "20":
        downloadAuthorTypeName = "初中高端网校通"
    elif downloadId == "21":
        downloadAuthorTypeName = "初中中端网校通"
    elif downloadId == "22":
        downloadAuthorTypeName = "初中普通网校通"
    elif downloadId == "23":
        downloadAuthorTypeName = "高中高端网校通"
    elif downloadId == "24":
        downloadAuthorTypeName = "高中中端网校通"
    elif downloadId == "25":
        downloadAuthorTypeName = "高中中端网校通"
    elif downloadId == "4":
        downloadAuthorTypeName = "记点通道"
    elif downloadId == "7":
        downloadAuthorTypeName = "扫码通道"
    else:
        downloadAuthorTypeName = ""
    return downloadAuthorTypeName


# 根据名字返回相应ID
def getDownloadId(Name):
    if Name == "初中高端网校通":
        downloadId = "20"
    elif Name == "初中中端网校通":
        downloadId = "21"
    elif Name == "初中普通网校通":
        downloadId = "22"
    elif Name == "高中高端网校通":
        downloadId = "23"
    elif Name == "高中中端网校通":
        downloadId = "24"
    elif Name == "高中中端网校通":
        downloadId = "25"
    elif Name == "记点通道":
        downloadId = "4"
    elif Name == "扫码通道":
        downloadId = "7"
    else:
        downloadId = ""
    return downloadId


def getSoftInfo(softType):
    if softType == "0":
        getPoint = "0"
        getMoney = '0'
        getCash = '0'
        getIsSupply = '0'
        getBackMoneyRate = '0'
        getBackCashRate = '0'
    elif softType == "1":
        getPoint = '1'
        getMoney = '0'
        getCash = '0'
        getIsSupply = '0'
        getBackMoneyRate = '0'
        getBackCashRate = '0'
    elif softType == "2":
        getPoint = "2"
        getMoney = '0'
        getCash = '0'
        getIsSupply = '0'
        getBackMoneyRate = '0'
        getBackCashRate = '0'
    elif softType == "3":
        getPoint = "3"
        getMoney = '0'
        getCash = '0'
        getIsSupply = '0'
        getBackMoneyRate = '0'
        getBackCashRate = '0'
    elif softType == "4":
        getPoint = "4"
        getMoney = '0'
        getCash = '0'
        getIsSupply = '0'
        getBackMoneyRate = '0'
        getBackCashRate = '0'
    elif softType == "5":
        getPoint = "5"
        getMoney = '0'
        getCash = '0'
        getIsSupply = '0'
        getBackMoneyRate = '0'
        getBackCashRate = '0'
    elif softType == "6":  # 储值
        getPoint = "0"
        getMoney = str(random.randint(1, 10))
        getCash = '0'
        getIsSupply = '0'
        getBackMoneyRate = str(random.randint(1, 6) * 10)
        getBackCashRate = '0'
    elif softType == "7":  # 第三方
        getPoint = "0"
        getMoney = '0'
        getCash = str(random.randint(1, 20))
        getIsSupply = '0'
        getBackMoneyRate = '0'
        getBackCashRate = str(random.randint(1, 6) * 10)
    else:  # 高级点
        getPoint = "0"
        getMoney = '0'
        getCash = '0'
        getIsSupply = '1'
        getBackMoneyRate = '0'
        getBackCashRate = '0'

    return [getPoint, getMoney, getCash, getIsSupply, getBackMoneyRate, getBackCashRate]


# 获取当前时间
def getNowTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
