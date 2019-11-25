from multiprocessing import Process
from time import sleep, ctime


class MyProcess(Process):
    def __init__(self, value):
        self.value = value
        super().__init__()

    def fun1(self):
        sleep(self.value)
        print("第一次", ctime)

    def fun2(self):
        sleep(self.value)
        print("第二次", ctime)

    def run(self):
        self.fun1()
        self.fun2()


MyProcess(2).run()
