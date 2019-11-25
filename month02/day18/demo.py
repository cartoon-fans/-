import hashlib

passwd = "abc123"
hash = hashlib.md5()
hash.update(passwd.encode())
passwd = hash.hexdigest()
print(passwd)
