"""
自定义线程类
"""
from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs={}):
        super().__init__()  # 此行不能动
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args, **self.kwargs)


####################################################
# 测试函数
def player(sec, song):
    for i in range(3):
        print("Playing %s : %s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={'song': '凉凉'})
t.start()  # 以一个线程去执行player函数
t.join()
