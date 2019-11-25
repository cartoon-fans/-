from gild import *
import time
from threading import Thread
from multiprocessing import Process

# 7.117348670959473  正常单进程　计算密集
# 4.382739305496216 正常单进程io密集
# 3.916379451751709   多进程　计算密集  有提升
# 4....  2...       多进程　io 密集 根据磁盘性能快慢不同
#  6.224767684936523　多线程　io  密集　有降低
# 8.594837665557861  多线程　计算密集　有降低
jobs=[]
start = time.time()
for i in range(10):
    p=Thread(target=count,args=(1,1))
    jobs.append(p)
    p.start()
[i.join() for i in jobs]
print(time.time() - start)


