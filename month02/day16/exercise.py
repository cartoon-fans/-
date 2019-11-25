import re

import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
# 生成游标对象（用于操作数据库数据，获取sql执行结果的对象）
cur = db.cursor()
# 执行各种数据库sql操作
file = open('dict.txt', 'r')
exe = []
for l in file:
    tup = re.findall(r"(\S+)\s+(.*)", l)[0]
    exe.append(tup)
file.close()
sql = "insert into words (word,mean) \
    values (%s,%s);"
try:
    cur.executemany(sql, exe)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
cur.close()
db.close()
