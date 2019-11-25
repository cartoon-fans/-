"""
regex2.py
match对象功能演示
"""

import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
m = regex.search('abcdefghi')

# 属性变量
# print(m.pos) # 目标字符串开头索引
# print(m.endpos)  # 目标字符串结尾索引
# print(m.re) # 正则表达式  ×
# print(m.string)  # 目标字符串
# print(m.lastgroup) # 最后一组组名 ×
# print(m.lastindex) # 最后一组序列号

# 属性方法
print(m.span()) # 匹配到的内容在目标字符串中的起止位置 ×
print(m.start())
print(m.end())
print(m.groupdict()) # 捕获组组名和对应匹配内容的字典 ×
print(m.groups()) # 获取所有子组对应的内容

print(m.group()) # 获取match对应内容  ×
print(m.group('pig'))












