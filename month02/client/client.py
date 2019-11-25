from socket import *

s = socket()
addr = ("172.40.74.189", 8888)
# addr = ("127.0.0.1", 8888)

s.connect(addr)
while True:
    data = input("输入内容>>")
    if not data:
        break
    s.send(data.encode())
    msg = s.recv(2048).decode()
    print(msg)

s.close()
