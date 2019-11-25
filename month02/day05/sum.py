from time import time
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

prime()