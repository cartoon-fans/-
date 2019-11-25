"""
chat room
* 发送请求，获取结果
"""

from socket import *
import os,sys

# 服务器地址
ADDR = ('127.0.0.1',8888)

def send_msg(s,name):
    while True:
        try:
            text = input("头像:")
        except KeyboardInterrupt:
            text = '##'
        if text == '##':
            msg = 'E ' + name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

def recv_msg(s):
    while True:
        try:
            data,addr = s.recvfrom(1024 * 1024)
        except KeyboardInterrupt:
            data = b'EXIT'
        # 收到EXIT时退出接收进程
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+'\n头像:',end='')

# 聊天
def chat(s,name):
    pid = os.fork()
    if pid < 0:
        os._exit(0)
    elif pid == 0:
        send_msg(s,name) # 子进程发消息
    else:
        recv_msg(s) # 父进程收消息


# 启动函数，构建网络链接
def main():
    s = socket(AF_INET,SOCK_DGRAM)

    # 进入聊天室
    while True:
        name = input("请输入姓名:")
        msg = "L " + name
        s.sendto(msg.encode(),ADDR)  # 发送请求
        data,addr = s.recvfrom(128) # 接收反馈
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())

    chat(s,name) # 聊天函数

if __name__ == '__main__':
    main()
