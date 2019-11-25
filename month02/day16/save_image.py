"""
存储二进制文件
"""
import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
# 生成游标对象（用于操作数据库数据，获取sql执行结果的对象）
cur = db.cursor()
# 执行各种数据库sql操作
# with open("lob.jpg", 'rb')as f:
#     data = f.read()
# try:
#     sql = "update class set img=%s where id=1;"
#     cur.execute(sql, [data])
#     db.commit()
# except:
#     db.rollback()
sql="select img from class where name='abby';"
cur.execute(sql)
data=cur.fetchone()
with open('abby.jpg','wb')as f:
    f.write(data[0])
cur.close()
db.close()
