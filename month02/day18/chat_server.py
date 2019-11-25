import os, sys
from socket import *

ADDR = ("0.0.0.0", 8888)

user = {}


def do_login(s, name, addr):
    if name in user:
        s.sendto("昵称已存在,请重新输入".encode(), addr)
        return
    s.sendto(b"OK", addr)  # 允许进入
    msg = "\n欢迎'%s'进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr


def do_chat(s, name, text):
    msg = "\n%s:%s" % (name, text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])


def do_exit(s, name):
    if name not in user:
        return
    msg = "\n%s退出聊天室" % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b"EXIT", user[i])
    del user[name]


def do_requst(s):
    while True:
        data, addr = s.recvfrom(1024)
        # 判断请求类型
        tmp = data.decode().split(" ", 2)  # 将请求拆分
        if tmp[0] == "L":
            do_login(s, tmp[1], addr)
        elif tmp[1] == "E":
            do_exit(s, tmp[1])
        elif tmp[2] == "C":
            do_chat(s, tmp[1], tmp[2])
        print(data)


def main():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid == 0:
        while True:
            msg = input("管理员消息")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(), ADDR)
    else:
        do_requst(s)


if __name__ == '__main__':
    main()
