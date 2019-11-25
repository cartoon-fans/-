from time import sleep
import os
# import signal
#
# signal.signal(signal.SIGCHLD, signal.SIG_SETMASK)


def foo():
    sleep(3)
    print("monidayin foo")


def bar():
    sleep(5)
    print("monidayin bar")


pid = os.fork()
if pid < 0:
    print("错误")
elif pid == 0:
    p2 = os.fork()
    if p2 == 0:
        foo()
    else:
        os._exit(0)
else:
    bar()
