"""
线程的属性设置
"""
from threading import Thread
from time import sleep


def fun():
    sleep(1)
    print("线程的属性测试")


t = Thread(target=fun, name="tedu")
t.setDaemon(True)
t.start()
t.setName("TEDU")
print("name:", t.getName())
print("is_alive", t.is_alive())
print(t.isDaemon())
# t.join()