from socket import *

sockfd = socket()
server_addr = ("127.0.0.1", 9526)
sockfd.connect(server_addr)
while True:
    data = input("输入文件地址")
    d = open(data, 'rb+')
    if not data:
        break
    sockfd.send(d.read())
    # if data == '#':
    #     break
    msg = sockfd.recv(1024)
    print("Server:", msg.decode())

sockfd.close()
