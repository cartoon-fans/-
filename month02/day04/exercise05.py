def find_dict(s):
    f = open("/home/tarena/桌面/dict.txt", "r")
    for line in f:
        tmp = line.split()[0]
        if tmp > s:
            f.close()
            return "没有找到该单词"
        if s == tmp:
            f.close()
            return  line
    else:
        f.close()
        return "找不到该单词"


from socket import *

socked = socket(AF_INET, SOCK_DGRAM)

socked.bind(("0.0.0.0", 6666))
while True:
    data, addr = socked.recvfrom(1024)
    msg=find_dict(data.decode())
    socked.sendto(msg.encode(), addr)
socked.close()
