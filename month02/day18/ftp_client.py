from socket import *
import sys
from time import sleep

ADDR = ("127.0.0.1", 8080)


class FTPClinet:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b"LIST")  # 发送请求
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            data = self.sockfd.recv(1024 * 1024).decode()
            print(data)
        else:
            print(data)

    def get_list(self, name):
        self.sockfd.send(("GET " + name).encode())
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            f = open("试下载/" + name, "wb")
            while True:
                data = self.sockfd.recv(1024)
                if data == b"##":
                    print("下载完成")
                    break
                f.write(data)
            f.close()
        else:
            print(data)

    def do_put(self, filename):
        try:
            f = open(filename, "rb")
        except Exception:
            print("该文件不存在", filename)
            return
        filename = filename.split("/")[-1]
        self.sockfd.send(("PUT " + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            while True:
                data = f.read(1024)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b"##")
                    print("上传完毕")
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)

    def exit(self):
        self.sockfd.send(b"EXIT")
        self.sockfd.close()
        sys.exit("谢谢使用")


def main():
    sockfd = socket()
    sockfd.connect(ADDR)
    ftp = FTPClinet(sockfd)
    while True:
        print("""\n======command======
      list
    get file
    put file
====================
      """)
        cmd = input("输入命令")
        if cmd == "list":
            ftp.do_list()
        elif cmd[:4] == "get ":
            filename = cmd.split(" ")[-1]
            ftp.get_list(filename)
        elif cmd[:4] == "put ":
            filename = cmd.split(" ")[-1]
            ftp.do_put(filename)
        elif cmd == "exit":
            ftp.exit()
        else:
            print("输入有误", cmd)
            # put 试下载 / zzz


if __name__ == '__main__':
    main()
