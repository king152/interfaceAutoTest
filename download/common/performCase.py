# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: performCase.py
@creatTime: 2019/09/17
"""

from download.models import TestCase, CaseResult, TestSoftId
from download.common.rollback import rollBackData
from download.common.inserts import initDate, initPoint, insertDate, getbate
from download.common.getCaseAttr import getNowTime, getDownloadId
from download.common.channel.initSnapshotData import insert_snapshots_table_data
from download.common.insertSql import initSoftPoint, updateDownloadDate, initDownloadDate, getStatus, getRebate, \
    getPoint
from download.common.tools import getRandom
from Logs.log import get_log
import time

log = get_log("performCase")


# 用例执行函数
def runCase(caseIds, username, project):
    if caseIds == 'all':
        allId = TestCase.objects.filter(newCaseUser=username, project=project).values('caseId')
        ids = []
        for d in allId:
            ids.append(d["caseId"])
    else:
        ids = caseIds.split(',')
        ids.reverse()
    for caseId in ids:
        try:
            Id = TestCase.objects.filter(caseId=caseId).values()
        except Exception as e:
            log.error(e)
        for d in Id:
            nowTime = getNowTime()
            route = getDownloadId(d['routeType'])
            initSoftPoint(d["softId"], d["softAuthorId"], d["addTime"], d["softPoint"],
                          d["softMoney"], d["softCash"], d["isSupply"], d["backCashRate"], d["backMoneyRate"])
            if d["ifLevel"] == "是":
                updateDownloadDate(d["softId"], d["wxtDownloadNumber"], d["pointDownloadNumber"],
                                   d["scanCodeDownloadNumber"], d["softPoint"])
            else:
                initDownloadDate(d["softId"], d["wxtDownloadNumber"], d["pointDownloadNumber"],
                                 d["scanCodeDownloadNumber"])
            guid = insert_snapshots_table_data(d["softPoint"], d["softMoney"], d["isSupply"], d["softCash"],
                                               d["backMoneyRate"], d["softAuthorId"], d["softId"],
                                               d["downloadAuthorId"],
                                               d["addTime"], route, d["backCashRate"])
            times = 0
            time.sleep(1)
            while True:
                if getStatus(d["softId"], nowTime) == 1:
                    # 返利结果判断
                    if d["functionPoint"] == '返利':
                        if getRebate(d["softId"], d["softAuthorId"], nowTime) == float(d['rebateAmount']):
                            CaseResult.objects.create(
                                caseId=d["caseId"],
                                caseName=d["caseName"],
                                rebateAmount=d['rebateAmount'],
                                assertResult=True,
                                executionTime=nowTime,
                                CaseExecutionResult="返利：{}".format(
                                    getRebate(d["softId"], d["softAuthorId"], nowTime)) + "--guid:" + str(guid),
                                guid=str(guid),
                                project=d["project"],
                                executionUser=username,
                                routeType=d["routeType"]
                            )
                            break
                        else:
                            CaseResult.objects.create(
                                caseId=d["caseId"],
                                caseName=d["caseName"],
                                rebateAmount=d['rebateAmount'],
                                assertResult=False,
                                executionTime=nowTime,
                                CaseExecutionResult="返利：{}".format(
                                    getRebate(d["softId"], d["softAuthorId"], nowTime)) + "--guid:" + str(guid),
                                guid=str(guid),
                                project=d["project"],
                                executionUser=username,
                                routeType=d["routeType"]
                            )
                            break
                    else:  # 升点结果判断
                        if int(getPoint(d["softId"])) == int(d["softPoint"]) + 1:  # 获取升点结果并进行判断
                            # 将结果写入数据库
                            CaseResult.objects.create(
                                caseId=d["caseId"],
                                caseName=d["caseName"],
                                rebateAmount=d['rebateAmount'],
                                assertResult=True,
                                executionTime=nowTime,
                                CaseExecutionResult="升点前：{}-后：{}".format(str(d["softPoint"]),
                                                                         str(getPoint(d["softId"]))) +
                                                    "返利：{}".format(getRebate(d["softId"], d["softAuthorId"],
                                                                             nowTime)) + "--guid:" + str(guid),
                                guid=str(guid),
                                project=d["project"],
                                executionUser=username,
                                routeType=d["routeType"]
                            )
                            break
                        else:
                            # 将结果写入数据库
                            CaseResult.objects.create(
                                caseId=d["caseId"],
                                caseName=d["caseName"],
                                rebateAmount=d['rebateAmount'],
                                assertResult=False,
                                executionTime=nowTime,
                                CaseExecutionResult="升点前：{}-后：{}".format(str(d["softPoint"]),
                                                                         str(getPoint(d["softId"]))) +
                                                    "返利：{}".format(getRebate(d["softId"], d["softAuthorId"],
                                                                             nowTime)) + "--guid:" + str(guid),
                                guid=str(guid),
                                project=d["project"],
                                executionUser=username,
                                routeType=d["routeType"]
                            )
                            break
                else:
                    times += 1
                    time.sleep(0.5)
                if times == 20:
                    # 服务器处理异常写入数据
                    CaseResult.objects.create(
                        caseId=d["caseId"],
                        caseName=d["caseName"],
                        rebateAmount=d['rebateAmount'],
                        assertResult=False,
                        executionTime=nowTime,
                        CaseExecutionResult="数据处理异常，请联系相关开发人员" + "--" + "guid:" + str(guid),
                        guid=str(guid),
                        project=d["project"],
                        executionUser=username,
                        routeType=d["routeType"]
                    )
                    break


# 异常步骤用例执行函数
def stepRunCase(Step, caseId):
    try:
        case = TestCase.objects.filter(caseId=caseId).values().first()
    except Exception as e:
        log.error(e)
    try:
        Guid = CaseResult.objects.filter(caseId=caseId).order_by("-executionTime").values().first()
    except Exception as e:
        log.error(e)
    route = getDownloadId(case['routeType'])
    result = rollBackData(step=Step, guid=Guid["guid"], softPoint=case["softPoint"], funcPoint=case["functionPoint"],
                          SchoolDown=case["wxtDownloadNumber"], PointDown=case["pointDownloadNumber"],
                          QcrDown=case["scanCodeDownloadNumber"], softAuthor=case["softAuthorId"], route=route)

    if result[0] == "返利":
        CaseResult.objects.filter(guid=Guid["guid"]).update(unusualStepResult=getRandom()+"_返利:" + str(result[1]))
    elif result[0] == "升点":
        CaseResult.objects.filter(guid=Guid["guid"]).update(
            unusualStepResult=getRandom()+"_提成：" + str(result[1]) + "-升点：" + str(result[2]))
    else:
        CaseResult.objects.filter(guid=Guid["guid"]).update(unusualStepResult=result[0]+'_'+getRandom())


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
