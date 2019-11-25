"""
进程池使用
1. 准备执行的事件函数
2. 创建进程池
3. 添加要执行的事件
4. 关闭，回收进程池
"""

from multiprocessing import Pool
from time import sleep,ctime

# 进程池事件函数
def worker(msg):
    sleep(2)
    print(ctime(),'--',msg)
    return "6666"

# 创建进程池
pool = Pool(4)

# 向进程池队列中添加事件
for i in range(10):
    msg = "Tedu %d"%i
    r = pool.apply_async(func=worker,args=(msg,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join()

print(r.get())





