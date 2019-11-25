from socket import *
import json
from settings import *
from threading import Thread


class Application:
    def __init__(self):
        self.sock = socket()
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sock.bind((frame_ip, frame_port))

    def start(self):
        self.sock.listen(3)
        print("Runing web serber on %s " % frame_port)
        while True:
            connfd, addr = self.sock.accept()
            t = Thread(target=self.handle, args=(connfd,))
            t.setDaemon(True)
            t.start()

    def handle(self, connfd):
        # 接受请求
        request = connfd.recv(1024).decode()
        if not request:
            return
        request = json.loads(request)  # json-->dict
        if request['method'] == "GET":
            if request['info'] == '/' or request["info"][-5:] == ".html":
                request=self.get_html(request['info'])
            else:
                pass
        elif request['method'] == "POST":
            pass
        #将数据发送给http server
        response=json.dumps(request)
        connfd.send(response.encode())
        connfd.close()
    # 处理网页
    def get_html(self, info):
        if info == '/':
            filename = STATIC_DIR + "/index.html"
        else:
            filename = STATIC_DIR + info
        try:
            fd = open(filename)
        except:
            return {"status":"404","data":open(STATIC_DIR+"/404.html").read()}
        else:
            return {"status": "200", "data":fd.read()}



if __name__ == '__main__':
    app = Application()
    app.start()
