"""
event 线程互斥方法
* 解决对共享资源的无序使用
"""
from threading import Thread,Event

# 用于线程间的通信 (共享资源 )
s = None

e = Event() # event对象

def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set() # 结束wait阻塞

t = Thread(target=杨子荣)
t.start()

print('说对口令就是自己人')
e.wait() # 阻塞等待 e.set()
if s == '天王盖地虎':
    print("宝塔镇河妖")
    print("确认过眼神,你是对的人")
else:
    print("打死他...")

t.join()











