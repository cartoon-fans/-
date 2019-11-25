"""
regex1.py  match对象生成者
"""

import re

s = "今年是2019年，建国70周年"
pattern = r'\d+'

# 返回匹配结果的迭代对象
it = re.finditer(pattern,s)
# 迭代到match对象（为了获取匹配内容更丰富的信息）
for i in it:
    print(i.group()) # 获取match对象对应的匹配内容

# 完全匹配一个字符串
m = re.fullmatch(r'.+',s)
print(m.group())

# 匹配字符串开头位置
m = re.match(r'\w+',s)
print(m.group())

#  匹配第一处
m = re.search(r'\d+',s)
print(m.group())

