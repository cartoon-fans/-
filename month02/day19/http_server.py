# 获取http请求
# 解析http请求
# 将请求发送给WebFrame
# 从WebFrame接收反馈数据
# 将数据组织为Response格式发送给客户端
from socket import *
from config import *
from select import *
import re
import json


def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip, frame_port))
    except:
        print("链接不到webframe")
        return
    # 发送数据
    data = json.dumps(env)
    s.send(data.encode())
    # 接受返回数据
    data = s.recv(1024 * 1024 * 10).decode()
    try:
        if  data:
            return json.loads(data)  # 返回一个字典
    except:
        return


# 封装http类
class HTTPSrever:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.address = (HOST, PORT)
        self.create_sicket()
        self.ep = epoll()
        self.fdmap = {}

    def create_sicket(self):
        self.sock = socket()
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sock.bind(self.address)

    def server_forever(self):
        self.sock.listen(3)
        print("您启动了http服务,监听%s端口" % self.port)
        self.ep.register(self.sock, EPOLLIN)
        self.fdmap[self.sock.fileno()] = self.sock
        while True:
            events = self.ep.poll()
            for k, v in events:
                if k == self.sock.fileno():
                    c, addr = self.fdmap[k].accept()
                    self.ep.register(c, EPOLLIN)
                    self.fdmap[c.fileno()] = c
                else:
                    self.handle(self.fdmap[k])
                    self.ep.unregister(k)
                    del self.fdmap[k]

    def handle(self, connfd):
        # 接受http请求
        request = connfd.recv(4096).decode()
        # 向webframe发送请求类型和请求内容
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern, request).groupdict()
        except:
            connfd.close()
            return
        else:
            data = connect_frame(env)
            if data:
                self.response(connfd, data)

    def response(self, connfd, data):
        # data:{"status":'200',"data":"ok"}
        if data["status"] == '200':
            # 网页存在
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += '\r\n'
            responseBody = data["data"]
        elif data["status"] == '404.html.html':
            # 网页不存在
            responseHeaders = "HTTP/1.1 404.html.html Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += '\r\n'
            responseHeaders += "Sorry...."
            responseBody = data["data"]

        response_data = responseHeaders + responseBody
        # 将结果发送给浏览器
        print(response_data)
        connfd.send(response_data.encode())


if __name__ == '__main__':
    httpd = HTTPSrever()
    httpd.server_forever()  # 启动服务
