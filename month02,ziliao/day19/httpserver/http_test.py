"""
检测httpserver
"""

from socket import *
import json

s = socket()
s.bind(('0.0.0.0',8080))
s.listen(3)
while True:
    c,addr = s.accept()
    data = c.recv(1024).decode()
    print(data)
    d = {'status':'200','data':'ok'}
    msg = json.dumps(d)
    c.send(msg.encode())