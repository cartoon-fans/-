"""
Lock 线程互斥方法
"""

from threading import Thread,Lock

lock = Lock()

a = b = 0 # 共享资源

# 线程函数
def value():
    while True:
        lock.acquire()
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release()

t = Thread(target = value)
t.start()

while True:
    with lock:    # 上锁处理
        a += 1
        b += 1
                  # 解锁处理
t.join()











