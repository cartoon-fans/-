"""
功能扩展标志
"""

import re

s = """Hello
北京
"""

# 只能匹配ascii编码
# regex = re.compile(r'\w+',flags=re.A)

# 忽略字母大小写
# regex = re.compile(r'[a-z]+',flags=re.I)

# . 可以匹配换行
# regex = re.compile(r'.+',flags=re.S)

# ^ $可以匹配每行开头结尾
regex = re.compile(r'^北京',flags=re.M)

l = regex.findall(s)
print(l)






