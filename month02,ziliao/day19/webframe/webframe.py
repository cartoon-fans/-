"""
webframe 配置文件

功能：
从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""
from socket import *
import json
from settings import *
from threading import Thread
from urls import *

# 将应用的功能封装在类中
class Application:
    def __init__(self):
        self.sock = socket()
        self.sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sock.bind((frame_ip,frame_port))

    def start(self):
        self.sock.listen(3)
        print("Running web server on %s"%frame_port)
        while True:
            connfd,addr = self.sock.accept()
            t = Thread(target=self.handle,args = (connfd,))
            t.setDaemon(True)
            t.start()

    def handle(self,connfd):
        # 接收请求
        request = connfd.recv(1024).decode()
        if not request:
            return
        request = json.loads(request) # json --> dict
        # request : {'method':'GET','info':'xxxxx'}
        if request['method'] == 'GET':
            if request['info'] == '/' or \
                    request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                # 获取某一种数据
                response = self.get_data(request['info'])
        elif request['method'] == 'POST':
            pass
        # 将数据发送给httpserer
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

    def get_html(self,info):
        if info == '/':
            filename = STATIC_DIR + '/index.html'
        else:
            filename = STATIC_DIR + info
        try:
            fd = open(filename)
        except:
            return {'status':'404','data':open(STATIC_DIR+'/404.html').read()}
        else:
            return {'status':'200','data':fd.read()}

    # 数据处理函数
    def get_data(self,info):
        for url,func in urls:
            if info == url:
                return {'status':'200','data':func()}
        return {'status': '404', 'data': 'Sorry'}


if __name__ == '__main__':
    app = Application()
    app.start() # 启动服务














