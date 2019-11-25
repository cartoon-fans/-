"""
   客户端数据： [
               (1,'Lily',10,78),
               (2,'Tom',9,91),
               (3,'Jame',8,80),
               (4,'Abby',11,87),
               (5,'Levi',9,76),
              ]
"""
from  socket import *
import struct

# 服务器地址
ADDR = ('127.0.0.1',8888)

data = [
           (1,'Lily',10,78),
           (2,'Tom',9,91),
           (3,'Jame',8,80),
           (4,'Abby',11,87),
           (5,'Levi',9,76),
        ]

# 确定数据格式
st = struct.Struct('i16sif')

# udp套接字
s = socket(AF_INET,SOCK_DGRAM)

for id,name,age,score in data:
    data = st.pack(id,name.encode(),age,score)
    s.sendto(data,ADDR)

s.close()



