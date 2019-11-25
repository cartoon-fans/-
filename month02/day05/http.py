from socket import *

ADDR = ("127.0.0.1", 8000)


# 处理http请求
def request(connfd):
    data = connfd.recv(4096).decode()
    if not data:
        return
    request_line = data.split('\n')[0]
    info = request_line.split(" ")[1]
    print(info)
    if info == "/":
        response = """HTTP/1.1 200  OK
        Content -Type:text/html

        
        """

        with open("index.html", "r") as f:
            response += f.read()

    else:
        response = """HTTP/1.1 404.html.html  Not Found
                Content -Type:text/html


                """
        response += "sorry...."
    connfd.send(response.encode())


# 搭建tcp网络，启动整个代码
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen()
    while True:
        connfd, addr = s.accept()
        request(connfd)


if __name__ == '__main__':
    main()
