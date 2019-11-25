filename = input("File:")

# 目标位置
file = filename.split('/')[-1]
new_file = "/home/tarena/" + file

try:
    fr = open(filename, 'rb')  # 二进制打开
except Exception as e:
    print(e)
else:
    fw = open(new_file, 'wb')
    # 循环的读写文件直到最后
    while True:
        data = fr.read(1024)  # 从源文件读
        if not data:
            break
        fw.write(data)  # 向新文件写
    fr.close()
    fw.close()
