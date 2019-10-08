# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: stepModel.py
@creatTime: 2019/08/29
"""

import time

from download.common.sqlOprate import MySqlServer

global STEP  # 连接ZxxkDownload数据库表
global ZXXK_LOG  # 连接zxxk_log数据库

STEP = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkDownload_ForTest')
ZXXK_LOG = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'Zxxk_Log_ForTest')


# 消费日志表 Zxxk_Log.dbo.Cl_ConsumeLog201908
def RecordConsumeLog(DownInfoID, Status, InfoID, consumeTime):
    '''
    :param DownInfoID: 步骤表guid
    :param Status: 状态
    :param InfoID: 资料softid
    :param consumeTime: 资料下载时间，与快照表插入时间一致
    :return:
    '''
    # 删除消费日志
    d_sql = "DELETE dbo.Cl_ConsumeLog201909 WHERE InfoID='{}' AND ConsumeTime='{}'".format(InfoID, consumeTime)
    ZXXK_LOG.insert_change_sql(d_sql)

    # 更新步骤状态语句
    updateSql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='RecordConsumeLog' AND DownInfoID='{}'".format(
        Status, DownInfoID)
    STEP.insert_change_sql(updateSql)


# 书城日志
def RecordBookShopLog(Status, DownInfoID):
    # 更新步骤状态语句
    updatesql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='RecordConsumeLog' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    # 执行更新命令
    STEP.insert_change_sql(updatesql)


# 通道类型下载量 Zxxk_Log.dbo.Cl_DownloadCountInfo
def RecordDowninterfaceHits(InfoID, SchoolDown, PointDown, QCRdown, softpoint, Status, DownInfoID):
    '''

    :param InfoID: 资料softID
    :param SchoolDown:网校通下载量
    :param PointDown:点数下载量
    :param QCRdown:扫码下载量
    :param softpoint:资料点数
    :param Status:步骤状态
    :param DownInfoID:步骤表guid
    :return:无
    '''
    # 1.数据回滚
    # 计算DownNum
    if InfoID == '4006829':
        if softpoint == '0':
            DownNum = 0
        elif softpoint == '1':
            DownNum = 21
        elif softpoint == '2':
            DownNum = 51
        elif softpoint == '3':
            DownNum = 71
        elif softpoint == '4':
            DownNum = 101
        else:
            pass
    else:
        DownNum = 'NULL'

    # 回滚执行数据库语句
    updateSql = "UPDATE dbo.Cl_DownloadCountInfo SET ShoolUserDownNum='{}',PointUserDownNum='{}',QRCodeUserDownNum='{}',DownNum={} WHERE InfoID='{}'".format(
        SchoolDown, PointDown, QCRdown, DownNum, InfoID)

    ZXXK_LOG.insert_change_sql(updateSql)

    # 2.修改步骤表步骤状态及数据
    # 更新步骤状态
    sqlServer = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkDownload_ForTest')  # 初始化数据库链接

    # 更新步骤状态语句
    stepSql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='RecordDowninterfaceHits' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    # 执行更新命令
    sqlServer.insert_change_sql(stepSql)

    # 关闭数据库连接
    sqlServer.close_sql()


# 资料升点下载量日志流水记录 select * from Zxxk_Log.dbo.Cl_SoftDownInfoLog
def RecordIncrePointFlowLog(InfoID, SoftPoint, Status, DownInfoID):
    '''
    :param InfoID: 资料softID
    :param SoftPoint: 资料点数
    :param Status: 状态
    :param DownInfoID: 步骤表guid
    :return:
    '''
    # 1.数据回滚

    # 查询资料下载数据
    q_sql = "select * from dbo.Cl_SoftDownInfoLog WHERE InfoID='{}' AND SoftPoint='{}'".format(InfoID, SoftPoint)

    data = ZXXK_LOG.query_sql(q_sql)
    if len(data) != 0:
        for d in data:
            DownCount = d[4]
        if DownCount > 1:
            u_sql = "UPDATE dbo.Cl_SoftDownInfoLog SET DownCount='' WHERE InfoID='' AND SoftPoint=''".format(DownCount - 1,
                                                                                                             InfoID,
                                                                                                             SoftPoint)
            ZXXK_LOG.insert_change_sql(u_sql)
        else:
            d_sql = "DELETE dbo.Cl_SoftDownInfoLog WHERE InfoID='' AND SoftPoint=''".format(InfoID, SoftPoint)
            ZXXK_LOG.insert_change_sql(d_sql)

    # 2.修改步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='RecordIncrePointFlowLog' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 更新资料下载量  select top 10 * from Zxxk_Hits.dbo.Cl_SoftDownloadHits
def UpdateSoftDownloadHit(softid, Status, DownInfoID):
    '''
    :param softid: 资料softID
    :param Status: 步骤表状态
    :param DownInfoID: 步骤表guid
    :return:
    '''
    # 1.数据回滚
    Zxxk_Hits = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'Zxxk_Hits')
    q_sql = "SELECT *FROM dbo.Cl_SoftDownloadHits WHERE SoftID='{}'".format(softid)
    data = Zxxk_Hits.query_sql(q_sql)
    if len(data) != 0:
        for d in data:
            Hits = d[2]
        if Hits > 1:
            u_sql = "UPDATE dbo.Cl_SoftDownloadHits SET Hits='' WHERE SoftID=''".format(Hits - 1, softid)
            Zxxk_Hits.insert_change_sql(u_sql)
        else:
            d_sql = "DELETE dbo.Cl_SoftDownloadHits WHERE SoftID='' ".format(softid)
            Zxxk_Hits.insert_change_sql(d_sql)
    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='UpdateSoftDownloadHit' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 获取 不发放 奖励的用户群组信息   select * from Zxxk.dbo.CID_Group a LEFT JOIN Zxxk.dbo.R_UserGroup b on a.groupid=b.groupid where b.userid=7926367
def GetFeedbackShieledUserGroupInfo(Status, DownInfoID):
    '''
    :param Status: 步骤表状态
    :param DownInfoID: 步骤表guid
    :return:
    '''
    # 1.数据回滚

    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='GetFeedbackShieledUserGroupInfo' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 记录免费和点数资料下载提成发放批次 select * from Zxxk_Log.dbo.Cl_FreePointDownFeeBackLog
def RecordFreePointDownFeeBackLog(UserID, AddTime, Status, DownInfoID):
    '''
    :param UserID:资料作者用户userid
    :param AddTime:下载时间
    :param Status:状态
    :param DownInfoID:步骤表guid
    :return:
    '''
    # 1.数据回滚
    d_sql = "DELETE FROM dbo.Cl_FreePointDownFeeBackLog WHERE UserID='{}'".format(UserID)
    ZXXK_LOG.insert_change_sql(d_sql)
    # 2 .步骤表状态更新
    u_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='RecordFreePointDownFeeBackLog' AND DownInfoID='{}'".format(
        Status, DownInfoID)
    STEP.insert_change_sql(u_sql)


# 记录月度优秀下载奖励批次发放日志  select * from Zxxk_Log.dbo.Cl_MonthlyExcellentDownFeeBackLog
def RecordMonthlyExcellentDownFeeBackLog(softid, Status, DownInfoID):
    # 1.数据回滚
    d_sql = "DELETE dbo.Cl_MonthlyExcellentDownFeeBackLog WHERE SoftID={}".format(softid)
    ZXXK_LOG.insert_change_sql(d_sql)

    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='RecordMonthlyExcellentDownFeeBackLog' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 月度优秀下载奖励发放 用户体系
def AssetIncreasedMonthlyExcellentDown(Status, DownInfoID):
    # 1.数据回滚

    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='AssetIncreasedMonthlyExcellentDown' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 下载提成发放 用户体系
def AsserIncreasedForNormalFeeBack(Status, DownInfoID):
    # 1.数据回滚

    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='AsserIncreasedForNormalFeeBack' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 月度优秀下载返利日志记录 select * from ZxxkAward.dbo.Cl_FeeBackLog2019  FeeBackBusinessType=1
def FeeBackLogForMonthly(Status, DownInfoID, Softid):
    # 1.数据回滚
    # SELECT *FROM ZxxkAward.dbo.Cl_FeeBackLog2019 WHERE FeeBackBusinessType='1' AND SoftID='4006829'
    Zxxk_Award = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkAward_ForTest')
    d_sql = "DELETE  dbo.Cl_FeeBackLog2019 WHERE FeeBackBusinessType='1' AND SoftID='{}'".format(Softid)
    Zxxk_Award.insert_change_sql(d_sql)

    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='FeeBackLogForMonthly' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 普通下载提成返利日志记录 select * from ZxxkAward.dbo.Cl_FeeBackLog2019  FeeBackBusinessType=0
def FeeBackLogForNormal(Status, DownInfoID, SoftId):
    # 1.数据回滚
    # SELECT *FROM ZxxkAward.dbo.Cl_FeeBackLog2019 WHERE FeeBackBusinessType='0' AND SoftID='4006829'
    Zxxk_Award = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkAward_ForTest')
    d_sql = "DELETE  dbo.Cl_FeeBackLog2019 WHERE FeeBackBusinessType='0' AND SoftID='{}'".format(SoftId)
    Zxxk_Award.insert_change_sql(d_sql)

    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='FeeBackLogForNormal' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 精品销售记录 select * from Zxxk_Log.dbo.Cl_CashSalesRecord
def RecordSellIncomeLog(Status, DownInfoID):
    # 1.数据回滚

    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='RecordSellIncomeLog' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 贡献点
def RecordUserGivePoint(Status, DownInfoID):
    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='RecordUserGivePoint' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 获取涨点屏蔽群组信息
def GetIncrePointShieledGroupInfo(Status, DownInfoID):
    # 1.数据回滚

    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='GetIncrePointShieledGroupInfo' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 获取升点规则信息 select * from Zxxk_Log.dbo.Cl_IncrePointRule
def GetIncrePointRuleInfo(Status, DownInfoID):
    # 1.数据回滚

    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}',StepResult=NULL WHERE StepName='GetIncrePointRuleInfo' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 更新资料点数 cl_soft
def UpdateSoftPoint(Status, DownInfoID, flag, softID, SoftPoint):
    # 1.数据回滚
    cl_soft = MySqlServer("10.1.5.70", 'zxxktest', '123456', 'ZxxkForDownloadTest')
    u_sql = sql = "UPDATE dbo.Cl_Soft SET SoftPoint='%s' WHERE SoftID='%s'" % (SoftPoint, softID)
    if flag == '返利':
        pass
    else:
        cl_soft.insert_change_sql(u_sql)
        cl_soft.close_sql()
    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='UpdateSoftPoint' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 涨点日志记录 select * from Zxxk_Log.dbo.Cl_PointIncreInfoLog
def RecordSoftPointIncreInfoLogAndUpdateDownNum(Status, DownInfoID, softid):
    # 1.数据回滚
    d_sql = "DELETE FROM dbo.Cl_PointIncreInfoLog WHERE  InfoID='{}'".format(softid)
    ZXXK_LOG.insert_change_sql(d_sql)

    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='RecordSoftPointIncreInfoLogAndUpdateDownNum' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 升点后记录下载量升点日志流水   select * from Zxxk_Log.dbo.Cl_SoftDownInfoLog
def RecordFlowLogAfterSoftPointIncre(Status, DownInfoID):
    # 1.数据回滚
    # select * from Zxxk_Log.dbo.Cl_SoftDownInfoLog WHERE InfoID='4006829' AND SoftPoint='5'
    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='RecordFlowLogAfterSoftPointIncre' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 更新用户下载量  用户体系（下载用户）
def UpdateUserDown(Status, DownInfoID):
    # 1.数据回滚
    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='UpdateUserDown' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 高端网校通日志（一年内）
def HighWXTConsumeLog(Status, DownInfoID, InfoID):
    """
    :param Status: 状态码
    :param DownInfoID: 快照表guid
    :param InfoID: 资料ID
    :return:
    """
    # 1.数据回滚
    nowMonth = time.strftime('%Y%m', time.localtime(time.time()))
    d_sql = "DELETE FROM dbo.Cl_WXTConsumeLog{} WHERE InfoID='{}'".format(nowMonth, InfoID)

    ZXXK_LOG.insert_change_sql(d_sql)
    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='HighWXTConsumeLog' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 高端网校通下载统计日志
def HighWxtDownLoadStatisticsLog(Status, DownInfoID, InfoID):
    # 1.数据回滚
    c_sql = "SELECT * FROM dbo.Cl_WXTDownLoadStatistics WHERE InfoID='{}'".format(InfoID)

    downC = ZXXK_LOG.query_sql(c_sql)
    if len(downC) != 0:
        DownCount = downC[0][2]
        tempCount = downC[0][3]
        if tempCount >= 1:
            u_sql = "UPDATE dbo.Cl_WXTDownLoadStatistics SET TempCount='{}' WHERE InfoID='{}'".format(tempCount - 1,
                                                                                                      InfoID)
            ZXXK_LOG.insert_change_sql(u_sql)
        else:
            u_sql = "UPDATE dbo.Cl_WXTDownLoadStatistics SET TempCount='99',DownCount='{}' WHERE InfoID='{}'".format(
                DownCount - 1, InfoID)
            ZXXK_LOG.insert_change_sql(u_sql)

    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='HighWxtDownLoadStatisticsLog' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 添加结算日志   SettlementLog2019  settlementlog201908
def AddSettlementLog(Status, DownInfoID):
    # 1.数据回滚
    # 2.步骤表状态
    step_sql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='AddSettlementLog' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    STEP.insert_change_sql(step_sql)


# 更新快照信息状态  status  1 成功 2 失败  ZxxkDownload	Cl_DownInfo
def UpdateDownInfoStatus(DownInfoID, Status):
    # 需要执行的数据库语句
    updateSql = "UPDATE dbo.B_StepInstanceInfo SET StepStatus='{}' WHERE StepName='UpdateDownInfoStatus' AND DownInfoID='{}'".format(
        Status, DownInfoID)

    # 执行更新步骤状态
    STEP.insert_change_sql(updateSql)

    # 更新快照表状态
    updateSnapshotSql = "UPDATE dbo.Cl_DownInfo SET Status='2' WHERE ID='{}'".format(DownInfoID)

    # 执行更新步骤状态
    STEP.insert_change_sql(updateSnapshotSql)


def closesql():
    # 关闭数据库链接
    STEP.close_sql()
    ZXXK_LOG.close_sql()
