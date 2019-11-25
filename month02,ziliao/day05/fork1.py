"""
fork1.py fork 进程演示
"""
import os
from time import sleep

print("============================")
a = 1

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Chile Process")
    print("a =",a)
    a = 10000
else:
    sleep(1)
    print("Parent Process")
    print("a:",a)

print("All a = ",a)