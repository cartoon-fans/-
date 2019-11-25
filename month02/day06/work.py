import os
from multiprocessing import Process

number = os.path.getsize("/home/tarena/桌面/log.txt")


one_size =number//2
two_size = number - one_size


def write1(name, size, pian):
    f = open("/home/tarena/桌面/log.txt", "r")
    n = open("/home/tarena/桌面/%s.txt" % name, "w+")

    f.seek(pian)
    n.write(f.read(size))
    f.close()
    n.close()
    print(n.name, "文件写入完成")


p = Process(target=write1, kwargs={"name": "two", "size": two_size, "pian": one_size})
p.start()
write1("one", one_size, 0)
p.join()
