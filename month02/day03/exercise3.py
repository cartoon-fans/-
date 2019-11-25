import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd.bind(("0.0.0.0", 9527))
sockfd.listen(3)
while True:
    print("等待链接...")
    try:
        connfd, addr = sockfd.accept()
        print("链接成功：", addr)
    except KeyboardInterrupt:
        break
    except EOFError as e:
        print(e)
        continue
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("收到", data.decode())
        n = connfd.send("收到".encode())
        print('发送了%d bytes' % n)

    connfd.close()
sockfd.close()
# data = connfd.recv(1024)
