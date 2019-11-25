"""
编写一个程序，向一个文件(log.txt)中不断写入内容
要求每2秒写入一行，每行内容：
       1.  2019-11-11 18:19:10
       2.  2019-11-11 18:19:12
       3.  2019-11-11 18:19:14
       4.  2019-11-11 18:36:18
如果程序结束，再次启动时要求序号能够衔接
"""

import time

f = open('log.txt','a+')

n = 0

# 文件偏移量到开头
f.seek(0)
for line in f:
    n += 1

while True:
    time.sleep(2)
    n += 1
    s = "%d.  %s\n"%(n,time.ctime())
    f.write(s)
    f.flush()  # 随时查看



