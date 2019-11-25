import time
from socket import *
import sys
import getpass

ADDR = ("127.0.0.1", 8080)

s = socket()
s.connect(ADDR)


def do_register():
    while True:
        name = input("输入注册用户名字")
        passwd = getpass.getpass("输入注册密码")
        passwd1 = getpass.getpass("重新输入注册密码")
        if passwd != passwd1:
            print("两次密码不一致")
            continue
        if " " in name or " " in passwd:
            print("帐号密码格式不正确")
            continue

        msg = "R %s %s" % (name, passwd)  # 发请求
        s.send(msg.encode())
        data = s.recv(128).decode()
        if data == "OK":
            print("注册成功")
        else:
            print(data)
            print("注册失败")
        return


def do_login():
    name = input("输入名字")
    passwd = getpass.getpass("输入密码")
    msg = "L %s %s" % (name, passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "OK":
        print("登录成功")
        two_view(name)
    else:
        print("登录失败")


def main():
    while True:
        print("""
        =========welcome===========
        1 注册   2 登陆    3 退出
        ===========================
                   """)
        cmd = input("输入指令")
        if cmd == "1":
            do_register()
        elif cmd == "2":
            do_login()
        elif cmd == '3':
            s.send(b'E')
            sys.exit("谢谢使用")
        else:
            print("请输入正确指令")


def do_note(name):
    msg = "H %s " % name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "OK":
        while True:
            data = s.recv(2048).decode()
            if data == '##':
                break
            print(data)

def two_view(name):
    while True:
        print("""
           ===========query===========
           1 查询单词   2 查询记录    3 注销
           ===========================
                      """)
        cmd = input("输入指令")
        if cmd == "1":
            do_query(name)
        elif cmd == "2":
            do_note(name)
        elif cmd == '3':
            return
        else:
            print("请输入正确指令")


def do_query(name):
    while True:
        word = input("单词:")
        if word == "##":
            break
        msg = "Q %s %s" % (name, word)
        s.send(msg.encode())
        data = s.recv(2048).decode()
        print(data)


if __name__ == '__main__':
    main()
