"""
select 用法示例
"""

from select import select
from socket import *
from time import sleep

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

f = open('log.txt','r+')

sleep(5)
print("监控IO")
rs,ws,xs = select([s,f],[f],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)












