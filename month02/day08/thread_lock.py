"""
lock 线程互斥方法
"""
from threading import Thread, Lock

a = b = 0
lock=Lock()


# 线程函数
def value():
    while True:
        lock.acquire()

        if a != b:
            print("bu相等", (a, b))
        lock.release()

t = Thread(target=value)
t.start()
while True:
    with lock:
        a += 1
        b += 1


t.join()
