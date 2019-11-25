import os
from multiprocessing import Pool, Queue

# os.mkdir("备份")
q = Queue()


def copy_text(i):
    f = open(i, "rb+")
    w = open("备份/%s备份" % i, "wb+")
    while True:
        n = w.write(f.read(256))
        if not n:
            break
        q.put(n)


pool = Pool()
size = 0
for i in os.listdir("./"):
    if i == "备份":
        continue
    pool.apply_async(func=copy_text, args=(i,))
    size += os.path.getsize(i)

pool.close()
pool.join()
copy_size = 0
while True:
    copy_size += q.get()
    print("拷贝了%0.1f%%数据" % (copy_size / size * 100))
