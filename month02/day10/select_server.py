"""
select_server.py tcp服务
"""
from socket import *
from select import select

# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8080))
s.listen(5)
rlist = [s]  # 关注 s的读事件
wlist = []
xlist = []
# 监控IO对应事件的发生
print("等待链接...")
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("客户端链接", addr)
            rlist.append(c)
        else:
            print("获取消息来自:", r.getpeername())
            data = r.recv(1024).decode()
            print(data)
            if not data:
                rlist.remove(r)
                r.close()
            # r.send(b"ok")
            wlist.append(r)
    for w in wlist:
        w.send(("收到").encode())
        wlist.remove(w)
