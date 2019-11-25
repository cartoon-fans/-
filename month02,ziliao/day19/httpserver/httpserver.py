"""
http server　部分的主体程序
功能：
获取http请求
解析http请求
将请求发送给WebFrame (请求类型和请求内容)
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
"""
from socket import *
from config import *
from select import *
import re
import json

# 用户和webframe交互
def connect_frame(env):
    """
    :param env: 要发送的字典
    :return: 从webframe得到的数据
    """
    s = socket()
    try:
        s.connect((frame_ip,frame_port))
    except:
        print("链接不到webframe")
        return
    # 发送字典 {'method':xxx,'info':...}
    data = json.dumps(env)
    s.send(data.encode())  # 数据 --》 webframe
    # 接收返回的数据
    data = s.recv(1024 * 1024 * 10).decode() #从webframe 接收
    try:
        if data:
            return json.loads(data)  # 返回一个字典
    except:
        return


# 封装ｈｔｔｐ类
class HTTPServer:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.address = (HOST,PORT)
        self.create_socket()
        #　ｅｐｏｌｌ需要的字典准备好
        self.fdmap = {}

    #　创建套接字
    def create_socket(self):
        self.sock = socket()
        self.sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sock.bind(self.address)

    #　启动函数
    def serve_forever(self):
        self.sock.listen(3)
        print("你启动了http服务，监听%s端口."%self.port)
        #　使用ｅｐｏｌｌ循环监听客户端链接
        self.ep = epoll()
        self.ep.register(self.sock, EPOLLIN)
        self.fdmap[self.sock.fileno()] = self.sock
        while True:
            events = self.ep.poll()
            for fd,evnet in events:
                if fd == self.sock.fileno():
                    connfd,addr = self.fdmap[fd].accept()
                    print("Connect from",addr)
                    self.ep.register(connfd,EPOLLIN)
                    self.fdmap[connfd.fileno()] = connfd
                else:
                    # 浏览器发送了http请求
                    self.handle(self.fdmap[fd]) # 长期占有服务端
                    self.ep.unregister(fd)
                    del self.fdmap[fd]
                    # data = self.fdmap[fd].recv(4096)
                    # print(data)

    def handle(self,connfd):
        # 接收http请求
        request = connfd.recv(4096).decode()
        # 向webframe 发送请求类型和请求内容
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern,request).groupdict()
        except:
            connfd.close()
            return
        else:
            data = connect_frame(env)
            if data:
                self.response(connfd,data)

    # 组织http响应给浏览器发送
    def response(self,connfd,data):
        # data: {'status':'200','data':'xxxxxxx'}
        if data['status'] == '200':
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']
        elif data['status'] == '404':
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']
        response_data = responseHeaders + responseBody
        connfd.send(response_data.encode())

if __name__ == '__main__':
    httpd = HTTPServer()
    httpd.serve_forever() #　启动服务












