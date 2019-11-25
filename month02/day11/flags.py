"""
功能扩展标志
"""
import re

s = """Hello
Hello
北京
"""
# 只能匹配ascii编码 A
# 不区分大小写 I
# 让.可以匹配换行 S
#让^$可以匹配每一行的开头结尾M
# regex = re.compile(r'\w+',flags=re.A)
# regex = re.compile(r'[a-z]+',flags=re.I)
# regex = re.compile(r'.+',flags=re.S)
regex = re.compile(r'^.+',flags=re.M)
l = regex.findall(s)
print(l)

