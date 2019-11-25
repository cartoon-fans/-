from threading import Thread
from socket import *
import sys, os
from time import sleep

HOST = '0.0.0.0'
RORT = 8080
ADDR = (HOST, RORT)
FTP = "/home/tarena/下载/"


class FTPserver(Thread):
    def __init__(self, commod):
        super().__init__()
        self.commod = commod

    def run(self):
        while True:
            data = self.commod.recv(1024).decode()
            print(data)
            if not data or data == "EXIT":
                return
            elif data == "LIST":
                self.do_list()
            elif data[:3] == "GET":
                filename = data.split(" ")[-1]
                self.do_get(filename)

            elif data[:3] == "PUT":
                filename = data.split(" ")[-1]
                self.do_put(filename)

    def do_list(self):
        files = os.listdir(FTP)
        if not files:
            self.commod.send("文件库为空".encode())
            return
        else:
            self.commod.send(b"OK")
            sleep(0.1)
        filelist = "\n".join(files)
        self.commod.send(filelist.encode())

    def do_get(self, name):
        try:
            f = open(FTP + name, "rb")
        except Exception:
            self.commod.send("无法下载".encode())
            return
        else:
            self.commod.send(b"OK")
            sleep(0.1)
        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)
                self.commod.send(b"##")
                break
            self.commod.send(data)
        f.close()

    def do_put(self, filename):
        if os.path.exists(FTP + filename):
            self.commod.send("文件已经存在".encode())
        else:
            self.commod.send(b"OK")
        f = open(FTP + filename, "wb")
        while True:
            data = self.commod.recv(1024)
            if data == b"##":
                break
            f.write(data)
        f.close()


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)
    print("等待链接")
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务退出")
        except Exception as e:
            print(e)
            continue
        t = FTPserver(c)
        t.setDaemon(True)  # 主线程服务退出，分支线程也退出
        t.start()


if __name__ == '__main__':
    main()
