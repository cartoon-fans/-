"""
模拟二级子进程
"""
from time import sleep
import os

def foo():
    sleep(3)
    print("模拟事件foo")

def bar():
    sleep(5)
    print("模拟事件bar")

p1 = os.fork()  # 创建一级子进程
if p1 == 0:
    p2 = os.fork() #  创建子进程的子进程
    if p2 == 0:
        # 二级子进程
        foo()
    else:
        os._exit(0)  # 一级子进程退出
else:
    os.wait()
    bar()




