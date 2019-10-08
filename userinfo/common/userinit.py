# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: userinit.py
@creatTime: 2019/09/20
"""

from download.models import SoftId
from userinfo.models import UserSoft


# 初始化用户数据，给每个注册用户分配500个资料id
def initUserSoftId(username):
    users_list = []
    start_id = SoftId.objects.all().values().first()['id']
    IDS = SoftId.objects.filter(id__lte=start_id+499).values()
    for ID in IDS:
        users_list.append(UserSoft(soft=ID['softId'],username=username))
    UserSoft.objects.bulk_create(users_list)
    SoftId.objects.filter(id__lte=start_id + 999).delete()