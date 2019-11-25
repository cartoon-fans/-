"""
算法转换
"""

import hashlib

passwd = 'abc123'

#　加盐处理　传入到ｍｄ()作为参数
salt = '*#06#'

hash = hashlib.md5(salt.encode()) #生成加密对象
hash.update(passwd.encode())  # 算法加密处理
passwd = hash.hexdigest() # 获取加密后的字串
print(passwd)
