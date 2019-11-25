"""
chat room
env: python3.6
socket  udp  & fork
"""

from socket import *
import os, sys

# 服务器地址
ADDR = ('0.0.0.0', 8888)

# 存储用户信息 {name:address}
user = {}

# 进入聊天室
def do_login(s, name, addr):
    if name in user or '管理员' in name:
        s.sendto('您的名字太受欢迎了'.encode(), addr)
        return
    s.sendto(b'OK', addr)  # 允许进入
    # 通知其他人
    msg = "\n欢迎 '%s' 进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr  # 加入字典


# 处理聊天
def do_chat(s, name, text):
    msg = "\n%s : %s" % (name, text)
    for i in user:
        # 刨除其自己
        if i != name:
            s.sendto(msg.encode(), user[i])

# 处理退出
def do_exit(s,name):
    # 防止用户不再user
    if name not in user:
        return
    msg = "\n%s 退出聊天室"%name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            # 他自己
            s.sendto(b'EXIT',user[i])
    del user[name] # 从字典中删除


# 接收请求，任务分发
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        # 判断请求类型 L   C    E
        tmp = data.decode().split(' ', 2)  # 将请求拆分
        if tmp[0] == 'L':
            do_login(s, tmp[1], addr)
        elif tmp[0] == 'C':
            do_chat(s, tmp[1], tmp[2])
        elif tmp[0] == 'E':
            do_exit(s,tmp[1])


# 网络搭建
def main():
    # udp服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid == 0:
        # 管理员消息发送
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员 "+msg
            s.sendto(msg.encode(),ADDR)
    else:
        # 接收客户端请求
        do_request(s)


if __name__ == '__main__':
    main()
