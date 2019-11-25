"""
multiprocessing 模块创建进程
"""

import multiprocessing as mp
from time import sleep

a = 1

# 进程函数
def fun():
    print("开始一个函数")
    sleep(2)
    global a
    print("a = ",a)
    a = 10000
    print("子进程结束")

# 创建进程对象
p = mp.Process(target=fun)
# 启动进程  执行fun
p.start()

sleep(3)
print("父进程也干点事")

# 回收进程
p.join()
print("a:",a)
print("==============================")

"""15--19行
p = os.fork()
if pid == 0:
    fun()
    os._exit()
else:
    os.wait()
"""



