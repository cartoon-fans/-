"""
空洞文件
"""

f = open('test','wb')
f.write(b'S')
f.seek(1024*1024,2)
f.write(b'E')
f.close()

