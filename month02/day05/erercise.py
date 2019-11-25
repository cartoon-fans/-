from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 8000))
s.listen()
c, addr = s.accept()
print("连接上了", addr)
data = c.recv(4096)

print(data.decode())
data = """HTTP/1.1 200  OK
Content -Type:text/html

hello world
"""
c.send(data.encode())
c.close()
s.close()
