"""regex1.py"""
import re

s = "今年是2019年,建国70周年"
pattern = r'\d+'
it = re.finditer(pattern, s)
# 每次迭代到的是一个match对象（为了获取匹配内容更丰富的信息）
for i in it:
    print(i.group())  # 获取match对象对应的匹配内容
# 完全匹配一个字符串
# m = re.fullmatch(r'.+', s)
# print(m.group())
# 匹配从开头的字符串
m = re.match(r'\w+', s)
print(m.group())

m = re.search(r'\d+', s)
print(m.group())

