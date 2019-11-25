"""
http_test.py
http请求响应演示
"""

from  socket import *

# http使用tcp传输
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8000))
s.listen()

c,addr = s.accept()
print("Connect from",addr)

# 收到http请求
data = c.recv(4096)
print(data.decode())

# 回复http响应
data = """HTTP/1.1 200 OK
Content-Type:text/html;charset=UTF-8

你好，新世界
"""
c.send(data.encode()) # 发送给浏览器

c.close()
s.close()


