"""
tcp_
"""
from socket import *

sockfd = socket()
server_addr = ("127.0.0.1", 9527)
sockfd.connect(server_addr)
while True:
    data = input(">>")
    if not data:
        break
    sockfd.send(data.encode())
    # if data == '#':
    #     break
    msg = sockfd.recv(1024)
    print("Server:", msg.decode())
sockfd.close()
