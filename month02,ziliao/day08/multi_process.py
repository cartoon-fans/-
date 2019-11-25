from GIL_test import *
from multiprocessing import Process
import time

jobs = []

tm = time.time()

for i in range(10):
    # p = Process(target=count,args=(1,1))
    p = Process(target=io)
    jobs.append(p)
    p.start()

[i.join() for i in jobs]

print("Process cpu:",time.time() - tm)


