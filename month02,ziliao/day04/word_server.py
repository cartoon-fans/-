"""
使用udp完成，在客户端可以循环的输入单词，然后得
到单词的解释。
单词本和服务端放在一起
"""
from socket import *

# 查找单词的功能
def find_word(word):
    # 默认r方式打开
    f = open('dict.txt')

    # 每次取一行
    for line in f:
        # 提取一行中的单词
        tmp = line.split(' ')[0]
        # 遍历的单词已经比目标大了
        if tmp > word:
            f.close()
            return "没有找到该单词"
        elif tmp == word:
            f.close()
            return line
    else:
        f.close()
        return "没有找到该单词"


# 创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
# 绑定地址
sockfd.bind(('0.0.0.0',8888))

# 收发消息
while True:
    data,addr = sockfd.recvfrom(64)
    # 查找单词
    msg = find_word(data.decode())
    # 查找到的单词解释
    sockfd.sendto(msg.encode(),addr)

sockfd.close()





