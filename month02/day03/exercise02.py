"""
buffer.py 文件写缓冲的机制
"""
# f = open("fuck", "w")
# while True:
#     data = input("输入内容")
#     if not data:
#         break
#     f.write(data)
#     f.flush()
# f.close()

# f = open("fuck", "w+")
# f.write("哇哦与改完额外俄方")
# f.seek(0)
# print(f.read())
# f.close()
import time

f = open("log.txt", "a+")

number = 0
f.seek(0)
for i in f:
    number += 1
while True:
    number += 1
    print(number, time.strftime("%Y-%m-%d  %H:%M:%S"))
    f.write(str(number) + "  " + str(time.strftime("%Y-%m-%d  %H:%M:%S")) + "\n")
    f.flush()
    time.sleep(2)
