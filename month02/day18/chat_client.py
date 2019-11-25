import sys
from socket import *
import os

ADDR = ("172.40.74.238", 8888)


def main():
    s = socket(AF_INET, SOCK_DGRAM)
    # 循环输入姓名　进入聊天室
    while True:
        name = input("请输入姓名")
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)  # 发送请求
        data, addr = s.recvfrom(128)
        if data.decode() == "OK":
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    chat(s, name)  # 聊天函数


def recv_msg(s):
    while True:
        try:
            msg, addr = s.recvfrom(1024)
        except KeyboardInterrupt:
            msg = b"EXIT"
        if msg.decode() == "EXIT":
            sys.exit()
        print(msg.decode(),'\n头像:',end='')

def send_msg(s, name):
    while True:
        try:
            text = input("头像")
        except KeyboardInterrupt:
            text = "##"
        if text == "##":
            msg = "E " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C " + name + ' ' + text
        s.sendto(msg.encode(), ADDR)


def chat(s, name):
    pid = os.fork()
    while True:
        if pid < 0:
            os._exit(0)  # 退出当前进程
        elif pid == 0:
            send_msg(s, name)
        else:
            recv_msg(s)


if __name__ == '__main__':
    main()
