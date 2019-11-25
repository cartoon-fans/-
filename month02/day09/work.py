"""
用fock来多进程并发
用process多进/线程并发
"""

# fork方法


# import signal
# import sys
# import os
# from socket import *
#
# s = socket()
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# s.bind(('0.0.0.0', 8888))
# s.listen(3)
# signal.signal(signal.SIGCHLD, signal.SIG_IGN)
# print("等待链接.........")
#
#
# def recv_send(c):
#     while True:
#         data = c.recv(1024).decode()
#         if not data:
#             break
#         print(data)
#         c.send(b"OK")
#     c.close()
#
#
# while True:
#     try:
#         c, addr = s.accept()
#         print("有客户端链接地址为", addr)
#     except KeyboardInterrupt:
#         s.close()
#         sys.exit("服务器退出")
#     except Exception as e:
#         print(e)
#         continue
#     pid = os.fork()
#
#     if pid == 0:
#         s.close()
#         recv_send(c)
#         sys.exit("客户端退出")
##################################################
# thread_server.py
from threading import Thread
from socket import *
import signal
import sys

s = socket()

s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("等待链接.........")

def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b"OK")
    c.close()


while True:
    try:
        c, addr = s.accept()
        print("有客户端链接", addr)
    except KeyboardInterrupt:
        sys.exit("服务断开")
    except Exception as e:
        print(e)
        continue
    t = Thread(target=handle, args=(c,))
    t.setDaemon(True)
    t.start()
