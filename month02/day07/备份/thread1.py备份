"""
threade1.py 线程基础使用
线程　　  封装线程函数
        创建线程对象
        启动线程
        回收线程
"""
import threading
from time import sleep
import os


def music():
    for i in range(3):
        sleep(2)
        print("播放黄河大合唱")


t = threading.Thread(target=music)
t.start()  # 启动线程
for i in range(4):
    sleep(1)
    print("播放：葫芦娃")
t.join()  # 启动线程
