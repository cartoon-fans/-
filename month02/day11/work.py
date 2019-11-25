# 利用正则表达式完成：
# 编写函数完成，从标准输入输入一个端口名称,返回该端口运行情况
# 描述中的address值（address is/Internet address is ）
import re

text = open("text", "r")
s = text.read()


def find_address():
    port = input("请输入端口名称")  # TenGigE0/0/1/0 /n/n
    list = re.split('\n\n', s)
    for i in list:
        if port == re.match(r"\S+", i).group():
            strings = i
            # print(strings)
            s1 = re.findall("address is.*|Internet address is .*", strings)
            obj=re.search(r"([0-9a-f]{4}\.){2}[[0-9a-f]{4}",strings).group()
            obj2=re.search(r'(\d{1,3}\.){3}\d{1,3}/\d{2}|Unknown',strings).group()

            print(obj)
            print(obj2)
            print(s1)
find_address()
