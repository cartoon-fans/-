from socket import *

sockfd = socket()
server_addr = ("172.40.91.205", 8888)
# server_addr = ("127.0.0.1", 8888)

sockfd.connect(server_addr)
while True:
    data = input(">>")
    if not data:
        break
    sockfd.send(data.encode())
    if data == '#':
        break
    msg = sockfd.recv(1024)
    print("Server:", msg.decode())
sockfd.close()
