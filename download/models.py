from django.db import models


class TestCase(models.Model):
    caseId = models.CharField(max_length=32)
    functionPoint = models.CharField(max_length=32, null=True)
    caseName = models.TextField(null=False)
    softId = models.CharField(null=True, max_length=32)
    softPoint = models.CharField(null=True, max_length=16)
    softMoney = models.CharField(null=True, max_length=16)
    softCash = models.CharField(null=True, max_length=16)
    isSupply = models.CharField(null=True, max_length=16)
    pointDownloadNumber = models.CharField(null=False, max_length=16)
    wxtDownloadNumber = models.CharField(null=False, max_length=16)
    scanCodeDownloadNumber = models.CharField(null=False, max_length=16)
    rebateAmount = models.CharField(max_length=64)
    addTime = models.DateTimeField()
    softAuthorId = models.CharField(null=True, max_length=32)
    downloadAuthorId = models.CharField(null=True, max_length=32)
    createTime = models.DateTimeField()
    caseNote = models.TextField(null=True)
    ifLevel = models.CharField(max_length=12, blank=True, null=True)
    newCaseUser = models.CharField(max_length=24, null=True, blank=True)
    project = models.CharField(max_length=64, null=True)
    routeType = models.CharField(max_length=32, null=True)
    backCashRate = models.CharField(null=True, max_length=16)
    backMoneyRate = models.CharField(null=True, max_length=16)


class CaseResult(models.Model):
    caseId = models.CharField(max_length=32)
    caseName = models.TextField(null=False)
    rebateAmount = models.CharField(max_length=64, null=False)
    assertResult = models.BooleanField(null=False)
    executionTime = models.DateTimeField(auto_now_add=True)
    CaseExecutionResult = models.TextField(null=True)
    unusualStepResult = models.TextField(null=True, blank=True)
    guid = models.CharField(max_length=64, null=True, blank=True)
    executionUser = models.CharField(max_length=24, null=True, blank=True)
    project = models.CharField(max_length=64, null=True)
    routeType = models.CharField(max_length=32, null=True)


class SoftId(models.Model):
    softId = models.IntegerField()


class TestSoftId(models.Model):
    softId = models.IntegerField()
    guid = models.CharField(max_length=128, blank=True, null=True)
    result = models.CharField(max_length=128, blank=True, null=True)
