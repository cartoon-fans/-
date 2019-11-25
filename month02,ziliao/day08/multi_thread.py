from GIL_test import *
from threading import Thread
import time

jobs = []

tm = time.time()

for i in range(10):
    # t = Thread(target=count,args=(1,1))
    t = Thread(target=io)
    jobs.append(t)
    t.start()

[i.join() for i in jobs]

print("Thread io:",time.time() - tm)


