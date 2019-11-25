"""
buffer.py  文件写缓冲机制

1.缓冲区被写满
2.程序执行结束或者文件对象被关闭
3.行缓冲遇到换行
4.程序中调用flush()函数
"""

# buffer = 1 为行缓冲
# f = open('test','w',1)
f = open('test','w')

while True:
    data = input(">>")
    if not data:
        break
    f.write(data)
    f.flush() # 人为的刷新缓冲
f.close()






