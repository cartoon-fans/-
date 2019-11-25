"""
套接字属性示例
"""

from socket import *

# 套接字
s = socket()

# 设置端口立即可以被重用,须在bind之前完成
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('0.0.0.0',8888))
s.listen(3)
c,addr = s.accept()

print("地址类型：",s.family)
print("套接字类型：",s.type)
print("套接字地址:",s.getsockname())
print("文件描述符:",s.fileno())
print("连接端地址:",c.getpeername())

c.recv(1024)



