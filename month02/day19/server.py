from socket import *
import json

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8080))
s.listen(3)

while True:
    print("等待客户端链接")
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
        continue
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print("收到", data, "地址", addr)
        d = {"status": '200', "data": "ok"}
        msg = json.dumps(d)
        c.send(msg.encode())
    c.close()
s.close()
