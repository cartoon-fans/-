"""
模拟僵尸进程产生
"""

import os,sys

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
    sys.exit(3)
else:
    """
    os.wait() 处理子进程退出状态
    """
    pid,status = os.wait()
    print("PID:",pid)
    print("status:",status) # 子进程退出状态 * 256
    while True:
        pass
