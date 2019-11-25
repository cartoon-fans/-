"""
seek.py  文件偏移量示例
"""

f = open('test','wb+') #读写

f.write(b"Hello wrold\n")
f.flush()
print("文件偏移量大小:",f.tell())

# 修改文件偏移量
f.seek(-7,2)
# f.write(b'hahahahah')

data = f.read()
print(data)

f.close()




