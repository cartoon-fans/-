from socket import *

ADDR = ('127.0.0.1', 6666)
sockfd = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input("word>>")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("解释", msg.decode())
