"""
求100000以内质数之和
分别使用4个进程和10个进程完成
查看执行所用时间

思路 : 将100000分成4份或者10份
      每个进程求其中一部分
"""
from time import time
from multiprocessing import Process

# 求运行时间装饰器
def timeit(f):
    def wrapper(*args,**kwargs):
        start_time = time()
        res = f(*args,**kwargs)
        end_time = time()
        print("%s函数执行时间:%.8f"%(f.__name__,end_time-start_time))
        return res
    return wrapper

# 判断一个数是否为质数
def isPrime(n:int)->bool:
    if n <= 1:
        return False
    for i in range(2,int(n)):
        if n % i == 0:
            return False
    return True

@timeit
def prime():
    pr = []
    for i in range(1,100001):
        if isPrime(i):
            pr.append(i)
    print("Sum:",sum(pr))

class Prime(Process):
    # 求从begin 到 end 之间的所有质数之和
    def __init__(self,pr,begin,end):
        """
        :param pr: list
        :param begin: int
        :param end: int
        """
        super().__init__()
        self.pr = pr
        self.begin = begin
        self.end = end

    def run(self):
        for i in range(self.begin, self.end):
            if isPrime(i):
                self.pr.append(i)
        print("Sum:", sum(self.pr))

@timeit
def use_4_process():
    prime=[]
    jobs = []
    for i in range(1,100001,25000):
        p = Prime(prime,i,i+25000)
        jobs.append(p)
        p.start()
    [process.join() for process in jobs]

@timeit
def use_10_process():
    prime=[]
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(prime,i,i+10000)
        jobs.append(p)
        p.start()
    [process.join() for process in jobs]

# prime()  # prime函数执行时间:26.17618990
# use_4_process() # use_4_process函数执行时间:14.79837823
use_10_process() # use_10_process函数执行时间:13.27693939






