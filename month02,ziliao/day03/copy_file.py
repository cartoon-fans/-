"""
编写程序完成：
用input输入一个文件名称（可以包含路径）
将这个文件拷贝到主目录下
注意： 文件可能文本文件也可能是二进制文件
要求： 文件不允许一次性读取
"""

# 输入文件名
filename = input("File:")

# 目标位置
file = filename.split('/')[-1]
new_file = "/home/tarena/" + file

try:
    fr = open(filename,'rb') # 二进制打开
except Exception as e:
    print(e)
else:
    fw = open(new_file,'wb')
    # 循环的读写文件直到最后
    while True:
        data = fr.read(1024) # 从源文件读
        if not data:
            break
        fw.write(data)  # 向新文件写
    fr.close()
    fw.close()

