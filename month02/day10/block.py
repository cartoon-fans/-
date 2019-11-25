"""
block_io.py
socket  套接字非阻塞示例
"""
from socket import *
from time import ctime, sleep
import os

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0',8888))
s.listen(3)
#设置套接字非阻塞行为
# s.setblocking(False)
f = open("log.txt", "a")
# 设置套接字阻塞时间
s.settimeout(2)
# print("Listen zhe port 8888...")
while True:
    print("Listen zhe port 8888...")
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except Exception as e:
        sleep(3)
        f.write("%s:%s\n" % (ctime(), e))
    s.close()
