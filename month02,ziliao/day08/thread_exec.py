"""
开启多个线程,分别从多个目标位置拷贝文件的不同部分,
然后在当前目录下合成一个完整的文件.
"""
import os
from threading import Thread,Lock

lock = Lock()
# 资源库
urls = [
    "/home/tarena/桌面/",
    "/home/tarena/公共的/",
    "/home/tarena/音乐/",
    "/home/tarena/视频/",
    "/home/tarena/模板/",
    "/home/tarena/下载/",
]

filename = input("要下载的文件:")
expr = [] # 存储哪些路径中有目标文件
for i in urls:
    if os.path.exists(i+filename):
        expr.append(i+filename)

path_num = len(expr) # 获取一共有几个资源
if path_num == 0:
    print("没有资源")
    os._exit(0)
file_size = os.path.getsize(expr[0]) # 要下载的文件大小
block_size = file_size // path_num + 1 # 每个线程需要拷贝的大小

# 待写入的文件 共享资源
fw = open(filename,'wb')

# 线程函数  path:从哪个资源位置拷贝, n:拷贝第几块
def load(path,n):
    fr = open(path,'rb')
    fr.seek(block_size * n)
    data = fr.read(block_size)
    with lock:
        fw.seek(block_size * n)
        fw.write(data)

jobs = []
n = 0
for path in expr:
    t = Thread(target=load,args=(path,n))
    jobs.append(t)
    t.start()
    n += 1

[i.join() for i in jobs]





























