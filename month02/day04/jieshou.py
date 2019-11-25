from socket import *
import struct


st = struct.Struct("i16sii")
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 9526))
f = open("student.txt", "a")
while True:
    data, addr = s.recvfrom(1024)
    tup = st.unpack(data)
    info = "%d  %s %d %d\n" % (
        tup[0], tup[1].decode().strip('\x00'), tup[2], tup[3])
    f.write(info)
f.close()
s.close()
