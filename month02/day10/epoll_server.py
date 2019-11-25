"""
pool_server.py 完成tcp并发
创建监听套接字
产生新的套接字也加入到监控中
"""
from socket import *
from select import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(5)
ep = epoll()
ep.register(s,EPOLLIN)
fdmap = {s.fileno(): s}
while True:
    events = ep.poll()
    for k, v in events:
        if k == s.fileno():
            c, addr = fdmap[k].accept()
            ep.register(c, EPOLLIN | EPOLLERR)
            fdmap[c.fileno()] = c
        elif v & EPOLLIN:
            data = fdmap[k].recv(1024).decode()
            if not data:
                ep.unregister(k)
                fdmap[k].close()
                del fdmap[k]
                continue
            print(data)
            fdmap[k].send(("收到").encode())
