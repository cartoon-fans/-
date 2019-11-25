"""
open_file.py
文件打开方式
规则：1 所有文件都可以用二进制方式打开读写
    2二进制文件不可以用文本方式打开读写

"""
# 文本方式打开文件读写数据都是字符串
# f = open("exercise.py", 'r', ) 只能读取 文件必须存在
# f = open("file", 'w') 不存在则创建 存在则清空文件内容
# f = open("file2", "a") 不存在则创建，存在不会清空原有内容 追加内容
# 二进制打开，读写都是字节串
# f = open("file", "r")
# date = f.readline()
# print(date)
# date = f.readlines(24)
# print(date)
# for item in date:
#     print(item)


# 操作文件
# print(f)
# 关闭文件
# f.close()
#
# f = open("/home/tarena/桌面/dict.txt", "r")
# s = input("请输入单词")
# for line in f:
#     tmp = line.split()[0]
#     if tmp >s:
#         print("没有找到该单词")
#         break
#     if s == tmp:
#         print(line)
#         break
# else:
#     print("找不到该单词")

#
# f = open("file", "w")
# # for i in range(500):
# #     f.write(str(i))
# #     f.write("\n")
# f.writelines(["abc\n", "你好\n", "北京\n "])
# f.close()
id = input("请输入一个文件路径")
f = open(id, "rb")
print(f)
# n = open("home/tarena/copy.jpg", "w")
# for item in f:
#     date = f.readline()
#     n.write(date)
#     if not date:
#         break
f.close()
n.close()
# with open("file")as f:
#     date = f.read()
#     print(date)


/home/tarena/桌面/xxx.jpg