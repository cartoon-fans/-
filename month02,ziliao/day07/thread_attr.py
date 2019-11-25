"""
线程属性设置
"""

from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun,name = "Tedu")

# 主线程退出分支线程也退出
t.setDaemon(True)

t.start()

t.setName("Tarena")
print("Name:",t.getName())
print("is alive:",t.is_alive())
print("Daemon:",t.isDaemon())














