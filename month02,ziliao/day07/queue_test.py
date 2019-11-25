"""
queue_test.py
消息队列功能演示
"""
from multiprocessing import Queue,Process
from time  import sleep
import os

q = Queue(3)

# 处理进程
def handle():
    data = q.get() # 读消息队列
    if data[1] == 'login':
        print("%d进程请求登录"%data[0])

# 请求进程
def request():
    print("请求登录")
    q.put((os.getpid(),'login')) # 写消息队列

p1 = Process(target=handle)
p2 = Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()










