"""
http_server.py
功能: 1. 获取来自浏览器的请求（request）
     2. 如果请求内容为'/'那么将 index.html给浏览器
     3. 如果不是'/' 返回给客户端404
"""
from socket import *

# 服务器地址
ADDR = ('127.0.0.1', 8888)


#  处理http请求
def request(connfd):
    # 获取http请求
    data = connfd.recv(1024 * 4).decode()
    if not data:
        return
    # 简单的解析
    request_line = data.split('\n')[0]
    info = request_line.split(' ')[1]  # 提取请求内容
    print("请求内容:",info)
    if info == '/':
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        with open('index.html') as f:
            response += f.read()
    else:
        response = "HTTP/1.1 404.html.html Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "Sorry...."
    # 将响应发送给浏览器
    connfd.send(response.encode())


# 搭建tcp网络，启动整个代码
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(3)
    while True:
        connfd, addr = sockfd.accept()
        request(connfd)


if __name__ == '__main__':
    main()
