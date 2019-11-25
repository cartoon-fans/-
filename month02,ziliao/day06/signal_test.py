"""
信号方法处理僵尸
"""

import os
import signal

# 子进程退出时父进程忽略，子进程由系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
    os._exit(3)
else:
    while True:
        pass