"""
进程对象属性
"""
from multiprocessing import Process
import time

def tm():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

# 进程对象
p = Process(target=tm,name="Tedu")

# 设置子进程随父进程退出 (start前设置)
p.daemon = True

p.start()

print("Name:",p.name)
print("PID:",p.pid)
print("is alive:",p.is_alive())
time.sleep(1)










