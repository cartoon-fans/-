"""
block_io.py
socket  套接字非阻塞示例
"""

from socket import *
from time import ctime,sleep

f = open('log.txt','a')  # 打开一个日志文件

# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 设置套接字非阻塞行为
# s.setblocking(False)

# 设置套接字超时时间
s.settimeout(2)


# 循环等待客户端链接
while True:
    print("Listen the port 8888...")
    try:
        c, addr = s.accept() # 超时等2s
    except Exception as e:
        sleep(3)
        f.write("%s : %s\n"%(ctime(),e))
    else:
        print("Connect from", addr)
        data = c.recv(1024)
        print(data)



s.close()

