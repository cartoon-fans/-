"""
regex.py  re模块示例
"""
import re

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"(\w+):(\d+)"

# re模块调用
l = re.findall(pattern,s)
print(l)

# compile对象调用
regex = re.compile(pattern)
l = regex.findall(s,0,14)
print(l)

# 使用正则表达式切割字符串
l = re.split(r':|,',s,2)
print(l)

# 替换正则匹配内容
s = re.sub(r'[^\w]','**',s,2)
print(s)
