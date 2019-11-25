"""
regex2.py
match 对象功能演示
"""
import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
m = regex.search("abcdefghi")
# 属性变量
print(m.pos)  # 目标字符串开头索引 0
print(m.endpos)  # 目标字符串结尾索引 9
print(m.re)  # 正则表达式  re.compile('(ab)cd(?P<pig>ef)')
print(m.string)  # 目标字符串 abcdefghi
print(m.lastgroup)  # 最后一组组名 pig
print(m.lastindex)  # 最后一组序列号 2
# 属性方法
print(m.span())  # 匹配到的内容位置 (0, 6)
print(m.start())  # 匹配到的内容开始位置 0
print(m.end())  # 匹配到的内容结束位置 6
print(m.groupdict())  # 获取捕获组组名和对应匹配内容{'pig': 'ef'} 字典
print(m.groups())  # 获取所有子组对应内容  ('ab', 'ef')元组
print(m.group())  # 获取match 对应内容 abcdef
print(m.group("pig"))  # 获取捕获组内容ef




