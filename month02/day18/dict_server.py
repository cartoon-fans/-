
from multiprocessing import Process
from socket import *
import sys, os
import signal
from time import sleep
from dict_date import *

HOST = '0.0.0.0'
RORT = 8080
ADDR = (HOST, RORT)

db = Datebase(user='root', password='123456', database='dict')


def do_register(c, name, passwd):
    if db.register(name, passwd):
        c.send(b"OK")
    else:
        c.send(b"Fail")


def do_login(c, name, passwd):
    if db.login(name, passwd):
        c.send(b"OK")
    else:
        c.send(b"Fail")


def do_query(c, name, word):
    db.insert_history(name, word)  # 插入历史记录
    mean = db.query(word)
    if not mean:
        c.send('没有找到该单词'.encode())
    else:
        msg = "%s : %s" % (word, mean)
        c.send(msg.encode())


def do_note(c, name):
    tup = db.note(name)
    if not tup:
        c.send('没有记录'.encode())
        return
    else:
        c.send(b"OK")
        for note in tup:
            msg = "%s %s %s" % note
            c.send(msg.encode())
        sleep(0.2)
        c.send(b"##")


def handle(c):
    db.create_cur()  # 每个子进程单独游标
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(), ":", data)
        tmp = data.split(" ")  # 解析请求
        if not data or tmp[0] == 'E':
            return
        elif tmp[0] == "R":
            do_register(c, tmp[1], tmp[2])
        elif tmp[0] == "L":
            do_login(c, tmp[1], tmp[2])
        elif tmp[0] == 'Q':
            # Q name word
            do_query(c, tmp[1], tmp[2])
        elif tmp[0] == 'H':
            # G name
            do_note(c, tmp[1])


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            db.close()
            sys.exit("服务退出")
        except Exception as e:
            print(e)
            continue
        p = Process(target=handle, args=(c,))
        p.daemon = True  # 主进程推出 子进程也推出
        p.start()


if __name__ == '__main__':
    main()
