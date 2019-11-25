from multiprocessing import Process
from socket import *
import sys,signal
HOST = '0.0.0.0'
RORT = 8888
ADDR = (HOST, RORT)
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("Listen zhe port 8888...")

def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b"OK")
    c.close()
while True:
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务退出")
    except Exception as e:
        print(e)
        continue
    p=Process(target=handle,args=(c,))
    p.daemon=True#主线程服务退出，分支线程也退出
    p.start()
