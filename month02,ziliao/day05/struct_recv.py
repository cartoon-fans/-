"""
提供一组数据，将该数据从客户端发送给服务端，
由服务端程序记录在一个文件中,每个学生信息占一行
文件名： student.txt
"""

from socket import *
import struct

# 确定struct格式
st = struct.Struct('i16sif')

# 创建udp套接字
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8888))

# 打开文件
f = open('student.txt','a')

# 循环读取，写入
while True:
    data,addr = s.recvfrom(1024)
    # 解包(1,b'Lily',14,78)
    tup = st.unpack(data)

    #写入内容
    info = "%d  %s  %d   %.1f\n"%(\
        tup[0],tup[1].decode().strip('\x00'),tup[2],tup[3])
    f.write(info)

f.close()
s.clsoe()






