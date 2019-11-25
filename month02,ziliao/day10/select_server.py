"""
select_server.py  tcp服务
重点代码

思路分析 : * 监控监听套接字的读事件
"""

from socket import *
from select import select

# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 设置关注列表
rlist = [s] # 关注s的读IO事件
wlist = []
xlist = []

# 循环监控IO对应事件发生
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    # 遍历返回值列表,根据情况讨论
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)  # 将c添加到读关注
        else:
            # 某个客户端套接字就绪 (某个客户端给我发消息)
            print("获取消息来自:",r.getpeername())
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r) # 将客户端对应套接字从关注的IO中移除
                r.close()
                continue
            print(data)
            # r.send(b'ok')
            wlist.append(r)  # 写关注

    # 处理写列表
    for w in ws:
        w.send(b'ok')
        wlist.remove(w) # 发完消息移除












