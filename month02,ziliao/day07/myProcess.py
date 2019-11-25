"""
自定义进程类演示
"""
from multiprocessing import Process
from time import sleep,ctime

class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()  # 加载父类__init__()

    def fun1(self):
        sleep(self.value)
        print("第一步：",ctime())

    def fun2(self):
        sleep(self.value)
        print("第二步：", ctime())

    # 流程控制
    def run(self):
        self.fun1()
        self.fun2()

p = MyProcess(2)
p.start()
p.join()








