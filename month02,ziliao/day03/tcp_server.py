"""
tcp_server.py
tcp 服务端最简流程

测试使用命令 ： telnet 127.0.0.1 8888
"""
import socket

# 创建TCP套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('127.0.0.1', 8888))

# 设置监听
sockfd.listen(3)

# 等待客户端链接
print("等待链接....")
connfd, addr = sockfd.accept()
print("链接了：",addr)

# 收发消息
data = connfd.recv(1024)
print("收到：",data)
n = connfd.send('收到'.encode()) # bytes
print("发送了 %d bytes"%n)

# 关闭套接字
connfd.close()
sockfd.close()


