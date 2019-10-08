# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: inserts.py
@creatTime: 2019/09/11
"""

import time
import uuid
from download.common.sqlOprate import MySqlServer, MySql

global INSERTDATE
global INITPOINT
global ZXXKLOG

INSERTDATE = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkDownload')
INITPOINT = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkForDownloadTest')

ZXXKLOG = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'Zxxk_Log')


# 插入快照表数据
def insertDate(SoftID):
    '''
    function:向快照表插入数据
    :param SoftPoint: 下载资料点数
    :param authorUserID:资料作者
    :param SoftID:资料id
    :param softinpuTime:资料上传时间
    :param DownloadUserID:下载用户id
    :return:
    '''
    id = uuid.uuid4()
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    DownInfo = '''{"eDownloadArgs": {
            "eSoft": {
                "ChannelID": 12,
                "ClassID": 610,
                "DepartmentID": 2,
                "SoftVersion": "全国通用",
                "SoftTypeID": 1,
                "SoftPoint": 2.00,
                "SoftPointConvertToRMB": 0.100,
                "SoftMoney": 0.00,
                "Hits": 16,
                "Elite": false,
                "Passed": true,
                "IsSupply": 0,
                "BackPointRate": 30,
                "BackMoneyRate": 40,
                "UserID": 28763241,
                "UserName": "测试资料",
                "InfoTitle": "测试资料为%s",
                "FileSize": 546,
                "Censor": "数学卢正发",
                "AdvPoint": 0,
                "IsBoutique": 0,
                "SourceID": 1,
                "SoftCash": 0.00,
            "SoftAsset": {
                "SoftCash": 0.00,
                "SoftMoney": 0.00,
                "SoftPoint": 2.00,
                "SoftPointConvertToRMB": 0.400,
                "AdvPoint": 0,
                "AdvPointConvertToRMB": 0.0,
                "Cash": 0.0,
                "IsBoutique": 0,
                "Type": 3,
                "PriceStr": "点数:2.00 点",
                "Price": 1.00,
                "IsFree": false
            },
            "ConsumeAsset": {
                "SoftCash": 0.0,
                "SoftMoney": 0.0,
                "SoftPoint": 2.00,
                "SoftPointConvertToRMB": 0.400,
                "AdvPoint": 0,
                "AdvPointConvertToRMB": 0.0,
                "Cash": 0.0,
                "IsBoutique": 0,
                "Type": 3,
                "PriceStr": "点数:2.00 点",
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
            "AddTime": "2019-08-24T08:23:00"
            },
        "eRequestArgs": {
            "Product": 1,
            "PlatFormType": 0,
            "RequestSource": 0,
            "QRCodeFee": 0.0,                           
            "UseRMB": 1,
            "ConsumeTime": "2019-09-10T08:23:00"
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
            "UserID": 28759633,
            "UserName": "xkw_028761111",
            "SchoolUserID": 0
            }
        },
    "Route": 4}''' % (SoftID, SoftID)
    insertsql = "INSERT INTO dbo.Cl_DownInfo (ID,UserID,SchoolID,SoftID,DownInfo,Instance,AddTime,Status) \
    VALUES('%s','28759633','0','%s','%s','0','%s','0')" % (id, SoftID, DownInfo, nowtime)
    INSERTDATE.insert_change_sql(insertsql)
    return id


# 初始化资料点数信息
def initPoint(softid):
    """
    function:初始化数据，将资源点数设置为测试数据一致
    :param softpoint: 资源点数
    :param softid: 资源id
    :return: 无
    """
    sql = "UPDATE dbo.Cl_Soft SET SoftPoint='2',AddTime='2019-08-24T08:23:00' WHERE SoftID='%s'" % (softid)  # 更新语句
    INITPOINT.insert_change_sql(sql)


# 初始化下载量
def initDate(InfoID):
    """
    function:设置资源下载次数
    :param InfoID: 资源id
    :param SchoolDown:网校通下载次数
    :param PointDown:普通用户下载次数
    :param QCRdown:扫码下载次数
    :return:无
    """
    # 删除下载量资料数据
    deletesql = "DELETE dbo.Cl_DownloadCountInfo WHERE InfoID=%s" % InfoID
    ZXXKLOG.insert_change_sql(deletesql)

    # 删除提成发放记录
    deleteissue = "DELETE dbo.Cl_FreePointDownFeeBackLog WHERE SoftID=%s" % InfoID
    ZXXKLOG.insert_change_sql(deleteissue)

    # 删除月度优秀奖励发放记录
    deletemonthlyissue = "DELETE dbo.Cl_MonthlyExcellentDownFeeBackLog WHERE SoftID=%s" % InfoID
    ZXXKLOG.insert_change_sql(deletemonthlyissue)

    # 插入数据
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    insertsql = "INSERT INTO dbo.Cl_DownloadCountInfo (InfoID,ShoolUserDownNum,PointUserDownNum,QRCodeUserDownNum,UpdateTime) VALUES('%s','5','5','6','%s')" % (
        InfoID, nowtime)
    ZXXKLOG.insert_change_sql(insertsql)


# 获取返利金额
def getbate(Softid):
    '''
    function:获取用户返利金额
    :param Userid: 返利用户userid
    :param exectime: 返利时间
    :return: sum(price[0:len(price)]) 返利金额
    '''
    mysql = MySql("10.1.1.6", 3306, "uc", "uc", "uc123")
    insersql = "SELECT * FROM T_IncomeRecord WHERE UserID='28763241' AND AddTime>='2019-09-12 10:00:00'  AND Remark LIKE '%{}%'".format(
        Softid)
    # number = 0
    # price = []
    # while True:
    #     if sum(price[0:len(price)]) == 0:
    #         try:
    #             datas = mysql.query_sql(insersql)
    #         except Exception as e:
    #             print("查询异常", e)
    #         for data in datas:
    #             if Softid in data[7]:
    #                 price.append(data[3])
    #
    #         number += 1
    #         time.sleep(0.5)
    #     else:
    #         break;
    #     if number == 20:
    #         break;

    try:
        data = mysql.query_sql(insersql)
    except Exception as e:
        print("查询异常", e)
    mysql.close_sql()
    for d in data:
        return d[3]


# 关闭数据库语句
def closallsql():
    INSERTDATE.close_sql()
    INITPOINT.close_sql()
    ZXXKLOG.close_sql()
