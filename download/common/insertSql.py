# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: insertSql.py
@creatTime: 2019/08/15
"""

import time
import uuid
import requests
from download.common.sqlOprate import MySqlServer, MySql
from Logs.log import get_log

log = get_log("TestCase")

'''
不发放奖励 用户ID：26628667，26431488，4684283

---不涨点：
1.不升点用户ID: 4684283，13794598，10006491，资料classId=668, 1419, 850, 538, 4963, 1251, 5037, 4974, 1155
2. 资料栏目为理综，文综（classId=5247, 5248 ）,且上传用户为“蒋琳zok,mayanquan,zy1868,731486168,sunxinwei821,李辰辰”，不涨点
'''


# 初始化资料点数信息
def initSoftPoint(softId, authorId, AddTime, softPoint=0.00, softMoney=0.00, softCash=0.00, isSupply=0,
                  backCashRate=0, backMoneyRate=0):
    """
    function:初始化数据，将资源点数设置为测试数据一致
    :param isSupply: 高级点资料标识
    :param softCash: 第三方资料价格
    :param softMoney: 储值资料价格
    :param backMoneyRate: 储值资料返现比
    :param backCashRate:第三方资料返现比
    :param AddTime:资料上传时间
    :param authorId:资料上传者
    :param softPoint: 资源普通点数
    :param softId: 资源id
    :return: 无
    """
    sqlServer = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkForDownloadTest')
    NormalLevelSql = "UPDATE dbo.Cl_Soft SET softPoint='{}', softMoney='{}', softCash='{}', \
         isSupply='{}', backCashRate='{}', backMoneyRate='{}',authorId='{}', \
         AddTime='{}' WHERE SoftID='{}'".format(softPoint, softMoney, softCash, isSupply,
                                                backCashRate, backMoneyRate, authorId,
                                                AddTime, softId)  # 正常升点更新

    NoLevelSql = "UPDATE dbo.Cl_Soft SET softPoint='{}', softMoney='{}', softCash='{}', \
             isSupply='{}', backCashRate='{}', backMoneyRate='{}',authorId='{}', \
             AddTime='{}',ChannelID = '13',ClassID='668' WHERE SoftID='{}'".format(softPoint, softMoney, softCash,
                                                                                   isSupply, backCashRate,
                                                                                   backMoneyRate,
                                                                                   authorId, AddTime, softId)  # 不升点用户组

    SpecialLevelSql = "UPDATE dbo.Cl_Soft SET softPoint='{}', softMoney='{}', softCash='{}', \
                 isSupply='{}', backCashRate='{}', backMoneyRate='{}',authorId='{}', \
                 AddTime='{}',ChannelID = '19',ClassID='5248' WHERE SoftID='{}'".format(softPoint, softMoney, softCash,
                                                                                        isSupply, backCashRate,
                                                                                        backMoneyRate,
                                                                                        authorId, AddTime,
                                                                                        softId)  # 资料栏目为理综

    if authorId in ['4684283', '10006491']:  # 不升点用户组
        sqlServer.insert_change_sql(NoLevelSql)

    elif authorId in ['13794598']:  # 资料栏目为理综
        sqlServer.insert_change_sql(SpecialLevelSql)

    else:
        sqlServer.insert_change_sql(NormalLevelSql)

    sqlServer.close_sql()


# 初始化下载量
def initDownloadDate(InfoID, SchoolDown, PointDown, ScanDown):
    """
    function:设置资源下载次数
    :param ScanDown: 扫码下载次数
    :param InfoID: 资源id
    :param SchoolDown:网校通下载次数
    :param PointDown:普通用户下载次数
    :return:无
    """
    sqlServer = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'Zxxk_Log_ForTest')
    log.info("开始初始化资源下载量信息：InfoID：%s" % InfoID)

    # 删除下载量资料数据
    deleteSql = "DELETE dbo.Cl_DownloadCountInfo WHERE InfoID=%s" % InfoID
    sqlServer.insert_change_sql(deleteSql)
    log.info("删除下载量数据：InfoID：%s 完成" % InfoID)

    # 删除提成发放记录
    deleteIssue = "DELETE dbo.Cl_FreePointDownFeeBackLog WHERE SoftID=%s" % InfoID
    sqlServer.insert_change_sql(deleteIssue)

    # 删除月度优秀奖励发放记录
    deleteMonthlyIssue = "DELETE dbo.Cl_MonthlyExcellentDownFeeBackLog WHERE SoftID=%s" % InfoID
    sqlServer.insert_change_sql(deleteMonthlyIssue)

    # 插入数据
    log.info("开始插入资料下载量数据：InfoID：%s SchoolDown:%s PointDown:%s QCRdown:%s" % (InfoID, SchoolDown, PointDown, ScanDown))
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    insertSql = "INSERT INTO dbo.Cl_DownloadCountInfo (InfoID,ShoolUserDownNum,PointUserDownNum,QRCodeUserDownNum,UpdateTime) VALUES('%s','%s','%s','%s','%s')" % (
        InfoID, SchoolDown, PointDown, ScanDown, nowTime)
    sqlServer.insert_change_sql(insertSql)
    log.info("插入资料下载量数据：InfoID：%s SchoolDown:%s PointDown:%s 完成" % (InfoID, SchoolDown, PointDown))
    sqlServer.close_sql()


# 更新下载量
def updateDownloadDate(softId, SchoolDown, PointDown, ScanDown, softPoint):
    # 实例化数据库
    sqlServer = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'Zxxk_Log_ForTest')
    log.info("开始初始化资源下载量信息：InfoID：%s" % softId)

    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    updateSql = "UPDATE dbo.Cl_DownloadCountInfo SET ShoolUserDownNum='{}',PointUserDownNum='{}',QRCodeUserDownNum='{}',UpdateTime='{}' WHERE InfoID='{}'".format(
        SchoolDown, PointDown, ScanDown, nowTime, softId)

    delUpPointSql = "DELETE dbo.Cl_PointIncreInfoLog WHERE InfoID='{}' AND SoftPoint='{}'".format(softId,
                                                                                                  int(softPoint) + 1)

    if int(softPoint) == 0:
        # 删除下载量资料数据
        log.info("开始删除下载量数据：InfoID：%s" % softId)
        deleteSql = "DELETE dbo.Cl_DownloadCountInfo WHERE InfoID=%s" % softId
        sqlServer.insert_change_sql(deleteSql)
        log.info("删除下载量数据：InfoID：%s 完成" % softId)

        # 删除提成发放记录
        deleteIssue = "DELETE dbo.Cl_FreePointDownFeeBackLog WHERE SoftID=%s" % softId
        sqlServer.insert_change_sql(deleteIssue)

        # 删除月度优秀奖励发放记录
        deleteMonthlyIssue = "DELETE dbo.Cl_MonthlyExcellentDownFeeBackLog WHERE SoftID=%s" % softId
        sqlServer.insert_change_sql(deleteMonthlyIssue)

        # 删除升点记录
        sqlServer.insert_change_sql(delUpPointSql)

        # 插入数据
        log.info(
            "开始插入资料下载量数据：InfoID：%s SchoolDown:%s PointDown:%s QCRdown:%s" % (softId, SchoolDown, PointDown, ScanDown))
        insertSql = "INSERT INTO dbo.Cl_DownloadCountInfo (InfoID,ShoolUserDownNum,PointUserDownNum,QRCodeUserDownNum,UpdateTime) VALUES('%s','%s','%s','%s','%s')" % (
            softId, SchoolDown, PointDown, ScanDown, nowTime)
        sqlServer.insert_change_sql(insertSql)
        log.info("插入资料下载量数据：InfoID：%s SchoolDown:%s PointDown:%s 完成" % (softId, SchoolDown, PointDown))
    elif int(softPoint) == 1:
        sqlServer.insert_change_sql(updateSql)

        # 删除升点记录
        sqlServer.insert_change_sql(delUpPointSql)
    elif int(softPoint) == 2:
        sqlServer.insert_change_sql(updateSql)

        # 删除升点记录
        sqlServer.insert_change_sql(delUpPointSql)
    elif int(softPoint) == 3:
        sqlServer.insert_change_sql(updateSql)

        # 删除升点记录
        sqlServer.insert_change_sql(delUpPointSql)
    elif int(softPoint) == 4:
        sqlServer.insert_change_sql(updateSql)

        # 删除升点记录
        sqlServer.insert_change_sql(delUpPointSql)
    else:
        log.error("softPoint错误{}".format(softPoint))
    sqlServer.close_sql()


# 插入下载信息
def initdownload(softID, UserID):
    sqlserver = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'Zxxk_Log_ForTest')
    insertsql = '''INSERT INTO [dbo].[Cl_ConsumeLog201908] (
	[ChannelID],
	[InfoID],
	[Title],
	[UserID],
	[UserName],
	[SchoolUserID],
	[ConsumePoint],
	[ConsumeAdvPoint],
	[ConsumeMoney],
	[ConsumeTime],
	[UserDownIP],
	[Editor],
	[Censor],
	[IsBoutique],
	[SoftTypeID],
	[RequestSource],
	[PlatForm],
	[ConsumeType],
	[IpArea],
	[DownInterface],
	[UserAgent],
	[UserAgentMD5],
	[ClientInfo],
	[ConsumeRMB],
	[Product],
	[ConsumeCount],
	[IsComment],
	[AccountSource]
)
VALUES
	(
		'13',
		'{}',
		N'精品解析：【全国百强校】黑龙江省哈尔滨师范大学附属中学2018-2019学年高一下学期开学考试语文试题 人教版',
		'{}',
		N'king158',
		'288',
		'.00',
		'0',
		'5.00',
		'2019-08-08 10:09:27.263',
		N'36.110.49.98',
		N'学科网试题平台',
		N'学科网原创组委会',
		'1',
		'1',
		'0',
		'0',
		'1',
		N'北京市电信',
		'4',
		N'Mozilla_5.0__Windows_NT_10.0;_WOW64__AppleWebKit_537.36__KHTML,_like_Gecko__Chrome_63.0.3239.132_Safari_537.36',
		N'8068257D4BA0C713A0692FCCB3F228',
		N'ut-17086-VG5akdvtSY',
		'.00',
		'1',
		'0',
		'0',
		NULL
	);'''.format(softID, UserID)
    sqlserver.insert_change_sql(insertsql)
    sqlserver.close_sql()


# 插入快照数据
def insertSnapshotDate(SoftPoint, SoftMoney, isSupply, softCash, backMoneyRate, authorUserID, SoftID, DownloadUserID,
                       AddTime, route, backCashRate):
    """
    function:向快照表插入数据
    :param backCashRate: 现金返现比例
    :param AddTime:资料上传时间
    :param softCash:现金
    :param backMoneyRate:储值返现比例
    :param isSupply:高级点
    :param SoftMoney:储值
    :param route: 通道类型ID
    :param SoftPoint: 下载资料点数
    :param authorUserID:资料作者
    :param SoftID:资料id
    :param DownloadUserID:下载用户id
    :return:
    """
    guid = uuid.uuid4()
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sqlServer = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkDownload_ForTest')
    log.info("开始插入快照表数据：id：%s 资料作者UserID:%s" % (guid, authorUserID))

    if authorUserID in ['13794598']:
        DownInfo = '''{"eDownloadArgs": {
                    "eSoft": {
                        "ChannelID": 19,
                        "ClassID": 5248,
                        "DepartmentID": 2,
                        "SoftVersion": "全国通用",
                        "SoftTypeID": 1,
                        "SoftPoint": %s,
                        "SoftPointConvertToRMB": 0.100,
                        "SoftMoney": %s,
                        "Hits": 16,
                        "Elite": false,
                        "Passed": true,
                        "IsSupply": %s,
                        "BackPointRate": 30,
                        "BackMoneyRate": %s,
                        "backCashRate": %s,
                        "UserID": %s,
                        "UserName": "mayanquan",
                        "InfoTitle": "测试资料为-%s",
                        "FileSize": 546,
                        "Censor": "数学卢正发",
                        "AdvPoint": 0,
                        "IsBoutique": 0,
                        "SourceID": 1,
                        "SoftCash": %s,
                    "SoftAsset": {
                        "SoftCash": %s,
                        "SoftMoney": %s,
                        "SoftPoint": %s,
                        "SoftPointConvertToRMB": 0.200,
                        "AdvPoint": %s,
                        "AdvPointConvertToRMB": 0.0,
                        "Cash": 0.0,
                        "IsBoutique": 0,
                        "Type": 3,
                        "PriceStr": "点数:1.00 点",
                        "Price": 1.00,
                        "IsFree": false
                    },
                    "ConsumeAsset": {
                        "SoftCash": 0.00,
                        "SoftMoney": %s,
                        "SoftPoint": %s,
                        "SoftPointConvertToRMB": 0.200,
                        "AdvPoint": %s,
                        "AdvPointConvertToRMB": 0.0,
                        "Cash": 0.0,
                        "IsBoutique": 0,
                        "Type": 3,
                        "PriceStr": "点数:1.00 点",
                        "Price": 1.00,
                        "IsFree": false
                    },
                    "IsShowXkw": 0, 
                    "XkwSoftID": 0,
                    "EarnRmb": 0.0,
                    "EarnPoint": 0.0,
                    "GivePoint": 0,
                    "IsMonthPayed": false,
                    "InfoUpdays": 130,
                    "ZeroAndPointDownNum": 0,
                    "DownNumFeeBackType": 0,
                    "eDownloadCountInfo": null,
                    "SettlementLogPara": {
                        "IsUpdateDownloadHits": 0,
                        "IsIncrePoint": 0,
                        "FeeBackType": 0
                    },
                    "SoftID": %s,
                    "SoftName": "2018年武汉市",
                    "SoftSize": 546,
                    "FileAddress": "{ploaddir}2019-2/24/ZXXKCOM20190224080904807728.doc",
                    "UpdateTime": "2019-02-24T08:23:00",
                    "AddTime": "%s"
                    },
                "eRequestArgs": {
                    "Product": 1,
                    "PlatFormType": 0,
                    "RequestSource": 0,
                    "QRCodeFee": 0.0,                           
                    "UseRMB": 1,
                    "ConsumeTime": "%s"
                },
                "eClientInfo": {
                "ClientIP": "36.110.49.98",
                "IPArea": "北京市电信",
                "UserAgent": "Mozilla_5.0__Windows_NT_10.0;_WOW64__AppleWebKit_537.36__KHTML,_like_Gecko__Chrome_63.0.3239.132_Safari_537.36",
                "UserAgentMD5": "8068257D4BA0C713A0692FCCB3F228",
                "Ut": "ut-21-wQ5YX3CCbS",
                "PathInfo": null
                },
                "eViewUserIdentity": {
                    "UserID": %s,
                    "UserName": "xkw_028761111",
                    "SchoolUserID": 0
                    }
                },
            "Route": %s}''' % (SoftPoint, SoftMoney, isSupply, backMoneyRate, backCashRate, authorUserID, SoftID,
                               softCash, softCash, SoftPoint, SoftMoney, isSupply, SoftMoney, SoftPoint, isSupply,
                               SoftID, AddTime, nowTime, DownloadUserID, route)
    elif authorUserID in ['4684283', '10006491']:
        DownInfo = '''{"eDownloadArgs": {
                    "eSoft": {
                        "ChannelID": 13,
                        "ClassID": 668,
                        "DepartmentID": 2,
                        "SoftVersion": "全国通用",
                        "SoftTypeID": 1,
                        "SoftPoint": %s,
                        "SoftPointConvertToRMB": 0.100,
                        "SoftMoney": %s,
                        "Hits": 16,
                        "Elite": false,
                        "Passed": true,
                        "IsSupply": %s,
                        "BackPointRate": 30,
                        "BackMoneyRate": %s,
                        "backCashRate": %s,
                        "UserID": %s,
                        "UserName": "king158",
                        "InfoTitle": "测试资料为-%s",
                        "FileSize": 546,
                        "Censor": "数学卢正发",
                        "AdvPoint": 0,
                        "IsBoutique": 0,
                        "SourceID": 1,
                        "SoftCash": %s,
                    "SoftAsset": {
                        "SoftCash": %s,
                        "SoftMoney": %s,
                        "SoftPoint": %s,
                        "SoftPointConvertToRMB": 0.200,
                        "AdvPoint": %s,
                        "AdvPointConvertToRMB": 0.0,
                        "Cash": 0.0,
                        "IsBoutique": 0,
                        "Type": 3,
                        "PriceStr": "点数:1.00 点",
                        "Price": 1.00,
                        "IsFree": false
                    },
                    "ConsumeAsset": {
                        "SoftCash": 0.00,
                        "SoftMoney": %s,
                        "SoftPoint": %s,
                        "SoftPointConvertToRMB": 0.200,
                        "AdvPoint": %s,
                        "AdvPointConvertToRMB": 0.0,
                        "Cash": 0.0,
                        "IsBoutique": 0,
                        "Type": 3,
                        "PriceStr": "点数:1.00 点",
                        "Price": 1.00,
                        "IsFree": false
                    },
                    "IsShowXkw": 0, 
                    "XkwSoftID": 0,
                    "EarnRmb": 0.0,
                    "EarnPoint": 0.0,
                    "GivePoint": 0,
                    "IsMonthPayed": false,
                    "InfoUpdays": 130,
                    "ZeroAndPointDownNum": 0,
                    "DownNumFeeBackType": 0,
                    "eDownloadCountInfo": null,
                    "SettlementLogPara": {
                        "IsUpdateDownloadHits": 0,
                        "IsIncrePoint": 0,
                        "FeeBackType": 0
                    },
                    "SoftID": %s,
                    "SoftName": "2018年武汉市",
                    "SoftSize": 546,
                    "FileAddress": "{ploaddir}2019-2/24/ZXXKCOM20190224080904807728.doc",
                    "UpdateTime": "2019-02-24T08:23:00",
                    "AddTime": "%s"
                    },
                "eRequestArgs": {
                    "Product": 1,
                    "PlatFormType": 0,
                    "RequestSource": 0,
                    "QRCodeFee": 0.0,                           
                    "UseRMB": 1,
                    "ConsumeTime": "%s"
                },
                "eClientInfo": {
                "ClientIP": "36.110.49.98",
                "IPArea": "北京市电信",
                "UserAgent": "Mozilla_5.0__Windows_NT_10.0;_WOW64__AppleWebKit_537.36__KHTML,_like_Gecko__Chrome_63.0.3239.132_Safari_537.36",
                "UserAgentMD5": "8068257D4BA0C713A0692FCCB3F228",
                "Ut": "ut-21-wQ5YX3CCbS",
                "PathInfo": null
                },
                "eViewUserIdentity": {
                    "UserID": %s,
                    "UserName": "xkw_028761111",
                    "SchoolUserID": 0
                    }
                },
            "Route": %s}''' % (SoftPoint, SoftMoney, isSupply, backMoneyRate, backCashRate, authorUserID, SoftID,
                               softCash, softCash, SoftPoint, SoftMoney, isSupply, SoftMoney, SoftPoint, isSupply,
                               SoftID, AddTime, nowTime, DownloadUserID, route)
    else:
        DownInfo = '''{"eDownloadArgs": {
                    "eSoft": {
                        "ChannelID": 10,
                        "ClassID": 620,
                        "DepartmentID": 2,
                        "SoftVersion": "全国通用",
                        "SoftTypeID": 1,
                        "SoftPoint": %s,
                        "SoftPointConvertToRMB": 0.100,
                        "SoftMoney": %s,
                        "Hits": 16,
                        "Elite": false,
                        "Passed": true,
                        "IsSupply": %s,
                        "BackPointRate": 30,
                        "BackMoneyRate": %s,
                        "backCashRate": %s,
                        "UserID": %s,
                        "UserName": "mayanquan",
                        "InfoTitle": "测试资料为-%s",
                        "FileSize": 546,
                        "Censor": "数学卢正发",
                        "AdvPoint": 0,
                        "IsBoutique": 0,
                        "SourceID": 1,
                        "SoftCash": %s,
                    "SoftAsset": {
                        "SoftCash": %s,
                        "SoftMoney": %s,
                        "SoftPoint": %s,
                        "SoftPointConvertToRMB": 0.200,
                        "AdvPoint": %s,
                        "AdvPointConvertToRMB": 0.0,
                        "Cash": 0.0,
                        "IsBoutique": 0,
                        "Type": 3,
                        "PriceStr": "点数:1.00 点",
                        "Price": 1.00,
                        "IsFree": false
                    },
                    "ConsumeAsset": {
                        "SoftCash": 0.00,
                        "SoftMoney": %s,
                        "SoftPoint": %s,
                        "SoftPointConvertToRMB": 0.200,
                        "AdvPoint": %s,
                        "AdvPointConvertToRMB": 0.0,
                        "Cash": 0.0,
                        "IsBoutique": 0,
                        "Type": 3,
                        "PriceStr": "点数:1.00 点",
                        "Price": 1.00,
                        "IsFree": false
                    },
                    "IsShowXkw": 0, 
                    "XkwSoftID": 0,
                    "EarnRmb": 0.0,
                    "EarnPoint": 0.0,
                    "GivePoint": 0,
                    "IsMonthPayed": false,
                    "InfoUpdays": 130,
                    "ZeroAndPointDownNum": 0,
                    "DownNumFeeBackType": 0,
                    "eDownloadCountInfo": null,
                    "SettlementLogPara": {
                        "IsUpdateDownloadHits": 0,
                        "IsIncrePoint": 0,
                        "FeeBackType": 0
                    },
                    "SoftID": %s,
                    "SoftName": "2018年武汉市",
                    "SoftSize": 546,
                    "FileAddress": "{ploaddir}2019-2/24/ZXXKCOM20190224080904807728.doc",
                    "UpdateTime": "2019-02-24T08:23:00",
                    "AddTime": "%s"
                    },
                "eRequestArgs": {
                    "Product": 1,
                    "PlatFormType": 0,
                    "RequestSource": 0,
                    "QRCodeFee": 0.0,                           
                    "UseRMB": 1,
                    "ConsumeTime": "%s"
                },
                "eClientInfo": {
                "ClientIP": "36.110.49.98",
                "IPArea": "北京市电信",
                "UserAgent": "Mozilla_5.0__Windows_NT_10.0;_WOW64__AppleWebKit_537.36__KHTML,_like_Gecko__Chrome_63.0.3239.132_Safari_537.36",
                "UserAgentMD5": "8068257D4BA0C713A0692FCCB3F228",
                "Ut": "ut-21-wQ5YX3CCbS",
                "PathInfo": null
                },
                "eViewUserIdentity": {
                    "UserID": %s,
                    "UserName": "xkw_028761111",
                    "SchoolUserID": 0
                    }
                },
            "Route": %s}''' % (SoftPoint, SoftMoney, isSupply, backMoneyRate, backCashRate, authorUserID, SoftID,
                               softCash, softCash, SoftPoint, SoftMoney, isSupply, SoftMoney, SoftPoint, isSupply,
                               SoftID, AddTime, nowTime, DownloadUserID, route)
    insertSql = "INSERT INTO dbo.Cl_DownInfo (ID,UserID,SchoolID,SoftID,DownInfo,Instance,AddTime,Status) \
    VALUES('%s','%s','0','%s','%s','0','%s','0')" % (guid, DownloadUserID, SoftID, DownInfo, nowTime)
    sqlServer.insert_change_sql(insertSql)
    log.info("插入快照表数据：id：%s 资料作者UserID:%s 完成" % (guid, authorUserID))
    sqlServer.close_sql()
    return guid


# 获取返利金额
def getRebate(SoftId, UserId, executeTime):
    """
    function:获取用户返利金额
    :param SoftId: 资料ID
    :param UserId: 返利用户UserId
    :param executeTime: 返利时间
    :return: sum(price[0:len(price)]) 返利金额
    """
    mysql = MySql("10.1.1.6", 3306, "uc", "uc", "uc123")
    log.info("开始查询返利信息")
    insertSql = "SELECT *FROM T_IncomeRecord WHERE UserID='{}' AND AddTime>='{}'".format(UserId, executeTime)
    number = 0
    price = []
    while True:
        if sum(price[0:len(price)]) == 0:
            try:
                datas = mysql.query_sql(insertSql)
            except Exception as e:
                log.error("查询异常", e)
            for data in datas:
                if SoftId in data[7]:
                    price.append(data[3])
            log.info("查询返利金额完成，Income金额列表为:{}".format(price[0:len(price)]))
            log.info("返回返利总和：{}元".format(sum(price[0:len(price)])))
            number += 1
            time.sleep(0.5)
        else:
            break
        if number == 20:
            break
    mysql.close_sql()
    return sum(price[0:len(price)])


# 获取资料点数信息
def getPoint(softid):
    sqlserver = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkForDownloadTest')
    log.info("开始查询资料点数信息：softid：%s" % softid)
    querysql = "SELECT *FROM dbo.Cl_Soft WHERE SoftID='%s'" % softid
    datas = sqlserver.query_sql(querysql)
    sqlserver.close_sql()
    for data in datas:
        log.info("查询资料点数完成，返回点数信息：softid %s---%s" % (softid, data[29]))
        return data[29]


# 获取下载数据处理状态
def getStatus(softid, exectime):
    sqlserver = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkDownload_ForTest')
    log.info("开始查询资料状态，查询softid为：%s" % softid)
    querysql = "SELECT *FROM dbo.Cl_DownInfo WHERE SoftID='{}' AND AddTime>='{}'".format(softid, exectime)
    datas = sqlserver.query_sql(querysql)
    sqlserver.close_sql()
    log.info("查询资料状态完成，查询softid为：%s" % softid)
    for data in datas:
        log.info("查询资料{}的状态为：{}".format(softid, data[7]))
        return data[7]


# 获取资料数
def getSoftid(number):
    sqlserver = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkForDownloadTest')
    log.info("开始获取资料数据.....")
    sql = "SELECT TOP {} SoftID FROM dbo.Cl_Soft WHERE addtime > '2016-01-01'".format(number)
    data = sqlserver.query_sql(sql)
    log.info("获取资源数据完成...")
    sqlserver.close_sql()
    return data


def getSoftid_ordertime(number, starttime='2019-01-01', endtime='2019-02-01'):
    sqlserver = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'Zxxk')
    log.info("开始获取资料数据.....")
    sql = "SELECT TOP {} SoftID,SoftPoint,SoftMoney,AddTime FROM dbo.Cl_Soft WHERE (SoftPoint>0 OR SoftMoney>0) AND AddTime>'{}' AND AddTime<'{}';".format(
        number, starttime, endtime)
    data = sqlserver.query_sql(sql)
    log.info("获取资源数据完成...")
    sqlserver.close_sql()
    return data


def requestdata(userID, softID):
    url = "http://10.1.1.4:8093/User/DrawUserLearnBean"

    querystring = {"userID": userID, "userName": "king158", "softID": softID, "type": "1",
                   "callback": "jQuery110204073301145017112_1566441963399", "_": "1566441963476"}

    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Host': "10.1.1.4:8093",
        'Accept-Encoding': "gzip, deflate",
    }
    log.info(querystring)
    res = requests.request("GET", url, headers=headers, params=querystring)
