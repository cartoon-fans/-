"""
thread2.py 线程参数演示
"""

from threading import Thread
from time import sleep


def fun(sec, name):
    print("线程函数参数")
    sleep(sec)
    print("%s打印执行完毕" % name)


# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun, args=(2,), kwargs={"name": "tedu%s"%i})
    jobs.append(t)
    t.start()
[i.join() for i in jobs]
