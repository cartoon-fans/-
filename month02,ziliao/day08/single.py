from GIL_test import *
import time

tm = time.time()

for i in range(10):
    # count(1,1)
    io()

print("Single io:",time.time() - tm)