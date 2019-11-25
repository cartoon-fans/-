"""
Event 线程互斥方法
解决对共享资源的无序使用
"""
from threading import Event, Thread

# 线程间的通信
s = None

e=Event()
def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()

t = Thread(target=杨子荣)
t.start()
print("说对口令就是自己人")
e.wait()
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他")
t.join()
