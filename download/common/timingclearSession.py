# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: timingclearSession.py
@creatTime: 2019/09/18
"""

import os
import sched
import time

schedule = sched.scheduler(time.time, time.sleep)


def perform_command(cmd, inc):
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    os.system(cmd)

def timming_exe(cmd, inc=60):
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    schedule.run()

print("Clear up expire session by timer")
os.chdir('F:/xkwauto')
timming_exe("python manage.py clearsessions", 20)
