from multiprocessing import Process
from time import time, ctime


# 求运行时间装饰器
def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time()
        res = f(*args, **kwargs)
        end_time = time()
        print("%s函数执行时间:%.8f" % (f.__name__, end_time - start_time))
        return res

    return wrapper


# 判断一个数是否为质数
def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True


@timeit
def prime(one, two):
    pr = []
    for i in range(one, two):
        if isPrime(i):
            pr.append(i)
    print("Sum:", sum(pr))


class MyProcess(Process):
    def __init__(self, one, two):
        self.one = one
        self.two = two
        super().__init__()

    def run(self):
        prime(self.one, self.two)

jobs = []
for i in range(4):
    p = MyProcess(i * 25000, (i + 1) * 25000)
    p.start()
    jobs.append(p)
[p.join() for p in jobs]
