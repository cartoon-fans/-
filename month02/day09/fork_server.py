# fork_server.py  fork 多进程网络并发
# 重点代码
import signal
from socket import *
import os

HOST = '0.0.0.0'
RORT = 8888
ADDR = (HOST, RORT)
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)
# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("Listen zhe port 8888...")


# 与客户端交换信息
def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b"OK")
    c.close()


# 循环等待客户端链接


while True:
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        s.close()
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    pid = os.fork()
    if pid == 0:
        s.close()
        handle(c)
        os._exit(0)  # 处理完客户端请求　子进程推出
    c.close()
