from socket import *

socked = socket(AF_INET, SOCK_DGRAM)

socked.bind(("0.0.0.0", 6666))
while True:
    data, addr = socked.recvfrom(1024)
    print("收到消息", data.decode())
    socked.sendto(b"Receive your msg", addr)
socked.close()



