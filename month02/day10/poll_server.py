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
p = poll()
p.register(s, POLLIN)
# fdmap={}
fdmap = {s.fileno(): s}
while True:
    events = p.poll()
    print(events)
    for k, v in events:
        if k == s.fileno():
            c, addr = fdmap[k].accept()
            print("有客户端链接", addr)
            p.register(c, POLLIN | POLLERR)
            fdmap[c.fileno()] = c
        elif v & POLLIN:
            data = fdmap[k].recv(1024).decode()
            if not data:
                p.unregister(k)
                fdmap[k].close()
                del fdmap[k]
                continue
            print(data)
            fdmap[k].send(("收到").encode())
