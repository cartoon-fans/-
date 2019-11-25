"""
进程池使用
1,提前准备好事件函数
2,创建进程池
3,添加要执行的事件
4,关闭，回收进程池
"""
from multiprocessing import Pool
from time import sleep, ctime


# 进程池事件函数
def worker(msg):
    sleep(1)
    print(ctime(), '--', msg)


# 创建进程池
pool = Pool(4)
for i in range(10):
    msg = "Tedu%d" % i
    pool.apply_async(func=worker, args=(msg,))
pool.close()
pool.join()