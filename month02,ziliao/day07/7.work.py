# # 进程创建的两种方法进行总结
# from multiprocessing import Process
#
#
# def fun():  # 子
#     pass  # 子
#
#
# p = Process(target=fun)
# p.start()
# p.join()
# # 子进程只运行target绑定的函数部分,其余内容均是父进程
# # 执行内容。父进程往往只用来创建子进程回收子进程,
# # 具体事件由子进程完成。
#
# import os
# import signal
#
# signal.signal(signal.SIGCHLD, signal.SIG_IGN)  # 处理僵尸
# pid = os.fork()
# if pid < 0:
#     print("Error")
# elif pid == 0:
#     pass  # 子进程事件
# else:
#     pass  # 父进程事件
#     os._exit()
#     # 直接创建子进程　互相拥有独立空间　通过if 和pid来让父子进程
#     # 执行不同的事件
#
#     # 熟练线程创建的方法
from threading import Thread
import os


def fun1(name, number):
    print("%s线程测试第%d次" % (name, number), "pid", os.getpid())


t = Thread(target=fun1, args=("李先生",), kwargs={"number": 1})
f = Thread(target=fun1, args=("王先生",) ,kwargs={"number": 2})
k = Thread(target=fun1, args=("刘先生",) ,kwargs={"number": 3})
t.start()
t.join()
k.start()
k.join()
f.start()
f.join()