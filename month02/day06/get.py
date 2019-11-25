import os

pid = os.fork()
if pid < 0:
    print("错误")
elif pid == 0:
    print("pid", os.getpid())
    print("父pid", os.getppid())

else:
    print("子进程", pid)
    print("Fu进程", os.getpid())
