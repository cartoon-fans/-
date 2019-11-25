"""
使用Process方法，创建两个子进程去同时复制一个文件的上
      半部分和下半部分，并分别写入到一个新的文件中。

       获取文件大小： os.path.getsize()
"""

from multiprocessing import Process
import os

filename = "dili.jpg"
size = os.path.getsize(filename)

# 父进程打开 如果父进程中打来一个 IO，子进程从父进程
# 获取IO对象，那么父子进程实际使用的是同一个IO操作
# fr = open(filename,'rb')
# print(fr.fileno())

# 复制上半部分
def top():
    fr = open(filename,'rb')
    print(fr.fileno())

    fw = open('top.jpg','wb')
    data = fr.read(size//2)
    fw.write(data)
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    print(fr.fileno())

    fw = open('bot.jpg', 'wb')
    fr.seek(size//2,0)
    data = fr.read()
    fw.write(data)
    fr.close()
    fw.close()

p1 = Process(target=top)
p2 = Process(target=bot)
p2.start()
p1.start()
p1.join()
p2.join()






