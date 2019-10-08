import time
import uuid
import random
from Logs.log import get_log
from download.common.sqlOprate import MySqlServer

log = get_log("wxtChannel")

'''
不发放奖励 用户ID：26628667，26431488，4684283

---不涨点：
1.不升点用户ID: 4684283，13794598，10006491，资料classId=668, 1419, 850, 538, 4963, 1251, 5037, 4974, 1155
2. 资料栏目为理综，文综（classId=5247, 5248 ）,且上传用户为“蒋琳zok,mayanquan,zy1868,731486168,sunxinwei821,李辰辰”，不涨点
'''


# 插入快照数据
def insert_snapshots_table_data(softPoint, softMoney, isSupply, softCash, backMoneyRate, authorUserID, softID,
                                downloadUserID, addTime, route, backCashRate):
    """
    function:向快照表插入数据
    :param backCashRate: 现金返现比例
    :param addTime:资料上传时间
    :param softCash:现金
    :param backMoneyRate:储值返现比例
    :param isSupply:高级点
    :param softMoney:储值
    :param route: 通道类型ID
    :param softPoint: 下载资料点数
    :param authorUserID:资料作者
    :param softID:资料id
    :param downloadUserID:下载用户id
    :return:
    """
    guid = uuid.uuid4()
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sqlServer = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkDownload_ForTest')
    log.info("开始插入快照表数据：id：%s 资料作者UserID:%s" % (guid, authorUserID))
    userRbm = random.randint(0, 1)
    if route != "7":
        if (int(softPoint) == 0 and int(softMoney) == 0 and int(softCash) == 0 and int(isSupply) == 0) or int(
                softPoint) != 0:
            if userRbm == 0:  # 点数充足
                if authorUserID in ['13794598']:  # 资料栏目为理综，文综,不升点
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 19,
                                            "ClassID": 5248,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 0,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "zy1868",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 0,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 0,
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
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 0,
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
                                        "UseRMB": 0,
                                        "ConsumeTime": "%s"
                                    },
                                    "eClientInfo": {
                                    "ClientIP": "36.110.49.98",
                                    "IPArea": "北京市电信",
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        softPoint, authorUserID, softID, softPoint, softPoint, softID, addTime, nowTime,
                        downloadUserID, route)
                elif authorUserID in ['4684283', '10006491']:  # 不升点和返利用户
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 13,
                                            "ClassID": 668,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 0,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "king158",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 0,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 0,
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
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 0,
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
                                        "UseRMB": 0,
                                        "ConsumeTime": "%s"
                                    },
                                    "eClientInfo": {
                                    "ClientIP": "36.110.49.98",
                                    "IPArea": "北京市电信",
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        softPoint, authorUserID, softID, softPoint, softPoint, softID, addTime, nowTime,
                        downloadUserID, route)
                else:
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 10,
                                            "ClassID": 620,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 0,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "king158",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 0,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 0,
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
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 0,
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
                                        "UseRMB": 0,
                                        "ConsumeTime": "%s"
                                    },
                                    "eClientInfo": {
                                    "ClientIP": "36.110.49.98",
                                    "IPArea": "北京市电信",
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        softPoint, authorUserID, softID, softPoint, softPoint, softID, addTime, nowTime,
                        downloadUserID, route)
            else:  # 储值抵扣
                if authorUserID in ['13794598']:  # 资料栏目为理综，文综,不升点
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 19,
                                            "ClassID": 5248,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 0,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "zy1868",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 0,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 0,
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
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": %s,
                                            "AdvPoint": 0,
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
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        softPoint, authorUserID, softID, softPoint, softPoint, float(softPoint) / 5.00, softID, addTime,
                        nowTime, downloadUserID, route)
                elif authorUserID in ['4684283', '10006491']:  # 不升点和返利用户
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 13,
                                            "ClassID": 668,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 0,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "king158",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 0,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 0,
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
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": %s,
                                            "AdvPoint": 0,
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
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        softPoint, authorUserID, softID, softPoint, softPoint, float(softPoint) / 5.00, softID, addTime,
                        nowTime, downloadUserID, route)
                else:
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 10,
                                            "ClassID": 620,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 0,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "king158",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 0,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 0,
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
                                            "SoftMoney": 0.00,
                                            "SoftPoint": %s,
                                            "SoftPointConvertToRMB": %s,
                                            "AdvPoint": 0,
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
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        softPoint, authorUserID, softID, softPoint, softPoint, float(softPoint) / 5.00, softID, addTime,
                        nowTime, downloadUserID, route)
        elif int(softMoney) != 0:
            if authorUserID in ['13794598']:  # 资料栏目为理综，文综,不升点
                DownInfo = '''{"eDownloadArgs": {
                                    "eSoft": {
                                        "ChannelID": 19,
                                        "ClassID": 5248,
                                        "DepartmentID": 2,
                                        "SoftVersion": "全国通用",
                                        "SoftTypeID": 1,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "SoftMoney": %s,
                                        "Hits": 16,
                                        "Elite": false,
                                        "Passed": true,
                                        "IsSupply": 0,
                                        "BackPointRate": 20,
                                        "BackMoneyRate": %s,
                                        "backCashRate": 0,
                                        "UserID": %s,
                                        "UserName": "zy1868",
                                        "InfoTitle": "测试资料为-%s",
                                        "FileSize": 546,
                                        "Censor": "数学卢正发",
                                        "AdvPoint": 0,
                                        "IsBoutique": 0,
                                        "SourceID": 1,
                                        "SoftCash": 0.00,
                                    "SoftAsset": {
                                        "SoftCash": 0.00,
                                        "SoftMoney": %s,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "AdvPoint": 0,
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
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.0,
                                        "AdvPoint": 0,
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
                                "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                            "Route": %s}''' % (
                    softMoney, backMoneyRate, authorUserID, softID, softMoney, softMoney, softID, addTime,
                    nowTime, downloadUserID, route)
            elif authorUserID in ['4684283', '10006491']:  # 不升点和返利用户
                DownInfo = '''{"eDownloadArgs": {
                                    "eSoft": {
                                        "ChannelID": 13,
                                        "ClassID": 668,
                                        "DepartmentID": 2,
                                        "SoftVersion": "全国通用",
                                        "SoftTypeID": 1,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "SoftMoney": %s,
                                        "Hits": 16,
                                        "Elite": false,
                                        "Passed": true,
                                        "IsSupply": 0,
                                        "BackPointRate": 20,
                                        "BackMoneyRate": %s,
                                        "backCashRate": 0,
                                        "UserID": %s,
                                        "UserName": "king158",
                                        "InfoTitle": "测试资料为-%s",
                                        "FileSize": 546,
                                        "Censor": "数学卢正发",
                                        "AdvPoint": 0,
                                        "IsBoutique": 0,
                                        "SourceID": 1,
                                        "SoftCash": 0.00,
                                    "SoftAsset": {
                                        "SoftCash": 0.00,
                                        "SoftMoney": %s,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "AdvPoint": 0,
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
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "AdvPoint": 0,
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
                                "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                            "Route": %s}''' % (
                    softMoney, backMoneyRate, authorUserID, softID, softMoney, softMoney, softID, addTime,
                    nowTime, downloadUserID, route)
            else:
                DownInfo = '''{"eDownloadArgs": {
                                    "eSoft": {
                                        "ChannelID": 10,
                                        "ClassID": 620,
                                        "DepartmentID": 2,
                                        "SoftVersion": "全国通用",
                                        "SoftTypeID": 1,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "SoftMoney": %s,
                                        "Hits": 16,
                                        "Elite": false,
                                        "Passed": true,
                                        "IsSupply": 0,
                                        "BackPointRate": 20,
                                        "BackMoneyRate": %s,
                                        "backCashRate": 0,
                                        "UserID": %s,
                                        "UserName": "king158",
                                        "InfoTitle": "测试资料为-%s",
                                        "FileSize": 546,
                                        "Censor": "数学卢正发",
                                        "AdvPoint": 0,
                                        "IsBoutique": 0,
                                        "SourceID": 1,
                                        "SoftCash": 0.00,
                                    "SoftAsset": {
                                        "SoftCash": 0.00,
                                        "SoftMoney": %s,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "AdvPoint": 0,
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
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.0,
                                        "AdvPoint": 0,
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
                                "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                            "Route": %s}''' % (
                    softMoney, backMoneyRate, authorUserID, softID, softMoney, softMoney, softID, addTime,
                    nowTime, downloadUserID, route)
        elif int(softCash) != 0:
            if authorUserID in ['13794598']:  # 资料栏目为理综，文综,不升点
                DownInfo = '''{"eDownloadArgs": {
                                    "eSoft": {
                                        "ChannelID": 19,
                                        "ClassID": 5248,
                                        "DepartmentID": 2,
                                        "SoftVersion": "全国通用",
                                        "SoftTypeID": 1,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "SoftMoney": 0.00,
                                        "Hits": 16,
                                        "Elite": false,
                                        "Passed": true,
                                        "IsSupply": 0,
                                        "BackPointRate": 20,
                                        "BackMoneyRate": 0,
                                        "backCashRate": %s,
                                        "UserID": %s,
                                        "UserName": "zy1868",
                                        "InfoTitle": "测试资料为-%s",
                                        "FileSize": 546,
                                        "Censor": "数学卢正发",
                                        "AdvPoint": 0,
                                        "IsBoutique": 0,
                                        "SourceID": 1,
                                        "SoftCash": %s,
                                    "SoftAsset": {
                                        "SoftCash": %s,
                                        "SoftMoney": 0.00,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "AdvPoint": 0,
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
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.0,
                                        "AdvPoint": 0,
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
                                "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                            "Route": %s}''' % (
                    backCashRate, authorUserID, softID, softCash, softCash, softCash, softID, addTime,
                    nowTime, downloadUserID, route)
            elif authorUserID in ['4684283', '10006491']:  # 不升点和返利用户
                DownInfo = '''{"eDownloadArgs": {
                                    "eSoft": {
                                        "ChannelID": 13,
                                        "ClassID": 668,
                                        "DepartmentID": 2,
                                        "SoftVersion": "全国通用",
                                        "SoftTypeID": 1,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "SoftMoney": 0.00,
                                        "Hits": 16,
                                        "Elite": false,
                                        "Passed": true,
                                        "IsSupply": 0,
                                        "BackPointRate": 20,
                                        "BackMoneyRate": 0,
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
                                        "SoftMoney": 0.00,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "AdvPoint": 0,
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
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "AdvPoint": 0,
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
                                "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                            "Route": %s}''' % (
                    backCashRate, authorUserID, softID, softCash, softCash, softCash, softID, addTime,
                    nowTime, downloadUserID, route)
            else:
                DownInfo = '''{"eDownloadArgs": {
                                    "eSoft": {
                                        "ChannelID": 10,
                                        "ClassID": 620,
                                        "DepartmentID": 2,
                                        "SoftVersion": "全国通用",
                                        "SoftTypeID": 1,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "SoftMoney": 0.00,
                                        "Hits": 16,
                                        "Elite": false,
                                        "Passed": true,
                                        "IsSupply": 0,
                                        "BackPointRate": 20,
                                        "BackMoneyRate": 0,
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
                                        "SoftMoney": 0.00,
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.00,
                                        "AdvPoint": 0,
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
                                        "SoftPoint": 0.00,
                                        "SoftPointConvertToRMB": 0.0,
                                        "AdvPoint": 0,
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
                                "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                            "Route": %s}''' % (
                    backCashRate, authorUserID, softID, softCash, softCash, softCash, softID, addTime,
                    nowTime, downloadUserID, route)
        elif int(isSupply) != 0:
            if userRbm == 0:  # 点数充足
                if authorUserID in ['13794598']:  # 资料栏目为理综，文综,不升点
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 19,
                                            "ClassID": 5248,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 1,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "zy1868",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 1,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
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
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
                                            "AdvPointConvertToRMB": 1.00,
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
                                        "UseRMB": 0,
                                        "ConsumeTime": "%s"
                                    },
                                    "eClientInfo": {
                                    "ClientIP": "36.110.49.98",
                                    "IPArea": "北京市电信",
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        authorUserID, softID, softID, addTime, nowTime, downloadUserID, route)
                elif authorUserID in ['4684283', '10006491']:  # 不升点和返利用户
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 13,
                                            "ClassID": 668,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 1,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "king158",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 1,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
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
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
                                            "AdvPointConvertToRMB": 1.00,
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
                                        "UseRMB": 0,
                                        "ConsumeTime": "%s"
                                    },
                                    "eClientInfo": {
                                    "ClientIP": "36.110.49.98",
                                    "IPArea": "北京市电信",
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        authorUserID, softID, softID, addTime, nowTime, downloadUserID, route)
                else:
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 10,
                                            "ClassID": 620,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 1,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "king158",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 1,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
                                            "AdvPointConvertToRMB": 1.00,
                                            "Cash": 0.0,
                                            "IsBoutique": 0,
                                            "Type": 3,
                                            "PriceStr": "点数:1.00 点",
                                            "Price": 1.00,
                                            "IsFree": false
                                        },
                                        "ConsumeAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
                                            "AdvPointConvertToRMB": 1.00,
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
                                        "UseRMB": 0,
                                        "ConsumeTime": "%s"
                                    },
                                    "eClientInfo": {
                                    "ClientIP": "36.110.49.98",
                                    "IPArea": "北京市电信",
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        authorUserID, softID, softID, addTime, nowTime, downloadUserID, route)
            else:  # 储值抵扣
                if authorUserID in ['13794598']:  # 资料栏目为理综，文综,不升点
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 19,
                                            "ClassID": 5248,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 1,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "zy1868",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 1,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
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
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
                                            "AdvPointConvertToRMB": 1.00,
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
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        authorUserID, softID, softID, addTime, nowTime, downloadUserID, route)
                elif authorUserID in ['4684283', '10006491']:  # 不升点和返利用户
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 13,
                                            "ClassID": 668,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 1,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "king158",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 1,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
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
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
                                            "AdvPointConvertToRMB": 1.00,
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
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        authorUserID, softID, softID, addTime, nowTime, downloadUserID, route)
                else:
                    DownInfo = '''{"eDownloadArgs": {
                                        "eSoft": {
                                            "ChannelID": 10,
                                            "ClassID": 620,
                                            "DepartmentID": 2,
                                            "SoftVersion": "全国通用",
                                            "SoftTypeID": 1,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "SoftMoney": 0.00,
                                            "Hits": 16,
                                            "Elite": false,
                                            "Passed": true,
                                            "IsSupply": 1,
                                            "BackPointRate": 20,
                                            "BackMoneyRate": 30,
                                            "backCashRate": 0,
                                            "UserID": %s,
                                            "UserName": "king158",
                                            "InfoTitle": "测试资料为-%s",
                                            "FileSize": 546,
                                            "Censor": "数学卢正发",
                                            "AdvPoint": 1,
                                            "IsBoutique": 0,
                                            "SourceID": 1,
                                            "SoftCash": 0.00,
                                        "SoftAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
                                            "AdvPointConvertToRMB": 1.00,
                                            "Cash": 0.0,
                                            "IsBoutique": 0,
                                            "Type": 3,
                                            "PriceStr": "点数:1.00 点",
                                            "Price": 1.00,
                                            "IsFree": false
                                        },
                                        "ConsumeAsset": {
                                            "SoftCash": 0.00,
                                            "SoftMoney": 0.00,
                                            "SoftPoint": 0.00,
                                            "SoftPointConvertToRMB": 0.00,
                                            "AdvPoint": 1,
                                            "AdvPointConvertToRMB": 1.00,
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
                                    "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                "Route": %s}''' % (
                        authorUserID, softID, softID, addTime, nowTime, downloadUserID, route)
        else:
            log.error("程序出现异常！")
    else:
        scanCash = random.randint(1, 15)
        if authorUserID in ['13794598']:  # 资料栏目为理综，文综,不升点
            DownInfo = '''{"eDownloadArgs": {
                                "eSoft": {
                                    "ChannelID": 19,
                                    "ClassID": 5248,
                                    "DepartmentID": 2,
                                    "SoftVersion": "全国通用",
                                    "SoftTypeID": 1,
                                    "SoftPoint": %s,
                                    "SoftPointConvertToRMB": 0.00,
                                    "SoftMoney": %s,
                                    "Hits": 16,
                                    "Elite": false,
                                    "Passed": true,
                                    "IsSupply": %s,
                                    "BackPointRate": 20,
                                    "BackMoneyRate": %s,
                                    "backCashRate": %s,
                                    "UserID": %s,
                                    "UserName": "zy1868",
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
                                    "SoftPointConvertToRMB": 0.00,
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
                                    "SoftMoney": 0.00,
                                    "SoftPoint": 0.00,
                                    "SoftPointConvertToRMB": 0.00,
                                    "AdvPoint": 0,
                                    "AdvPointConvertToRMB": 0.0,
                                    "Cash": %s,
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
                            "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                        "Route": 7}''' % (
                softPoint, softMoney, isSupply, backMoneyRate, backCashRate, authorUserID, softID, softCash, softCash,
                softMoney, softPoint, isSupply, str(scanCash), softID, addTime, nowTime, downloadUserID)
        elif authorUserID in ['4684283', '10006491']:  # 不升点和返利用户
            DownInfo = '''{"eDownloadArgs": {
                                            "eSoft": {
                                                "ChannelID": 13,
                                                "ClassID": 668,
                                                "DepartmentID": 2,
                                                "SoftVersion": "全国通用",
                                                "SoftTypeID": 1,
                                                "SoftPoint": %s,
                                                "SoftPointConvertToRMB": 0.00,
                                                "SoftMoney": %s,
                                                "Hits": 16,
                                                "Elite": false,
                                                "Passed": true,
                                                "IsSupply": %s,
                                                "BackPointRate": 20,
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
                                                "SoftPointConvertToRMB": 0.00,
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
                                                "SoftMoney": 0.00,
                                                "SoftPoint": 0.00,
                                                "SoftPointConvertToRMB": 0.00,
                                                "AdvPoint": 0,
                                                "AdvPointConvertToRMB": 0.0,
                                                "Cash": %s,
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
                                        "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                    "Route": 7}''' % (
                softPoint, softMoney, isSupply, backMoneyRate, backCashRate, authorUserID, softID, softCash, softCash,
                softMoney, softPoint, isSupply, str(scanCash), softID, addTime, nowTime, downloadUserID)
        else:
            DownInfo = '''{"eDownloadArgs": {
                                            "eSoft": {
                                                "ChannelID": 10,
                                                "ClassID": 620,
                                                "DepartmentID": 2,
                                                "SoftVersion": "全国通用",
                                                "SoftTypeID": 1,
                                                "SoftPoint": %s,
                                                "SoftPointConvertToRMB": 0.00,
                                                "SoftMoney": %s,
                                                "Hits": 16,
                                                "Elite": false,
                                                "Passed": true,
                                                "IsSupply": %s,
                                                "BackPointRate": 20,
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
                                                "SoftPointConvertToRMB": 0.00,
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
                                                "SoftMoney": 0.00,
                                                "SoftPoint": 0.00,
                                                "SoftPointConvertToRMB": 0.00,
                                                "AdvPoint": 0,
                                                "AdvPointConvertToRMB": 0.0,
                                                "Cash": %s,
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
                                        "UserAgent": "Mozilla_5.0__Windows_NT_10.0;",
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
                                    "Route": 7}''' % (
                softPoint, softMoney, isSupply, backMoneyRate, backCashRate, authorUserID, softID, softCash, softCash,
                softMoney, softPoint, isSupply, str(scanCash), softID, addTime, nowTime, downloadUserID)

    insertSql = "INSERT INTO dbo.Cl_DownInfo (ID,UserID,SchoolID,SoftID,DownInfo,Instance,AddTime,Status) \
    VALUES('%s','%s','0','%s','%s','0','%s','0')" % (guid, downloadUserID, softID, DownInfo, nowTime)
    sqlServer.insert_change_sql(insertSql)
    log.info("插入快照表数据：id：%s 资料作者UserID:%s 完成" % (guid, authorUserID))
    sqlServer.close_sql()
    return guid
