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
sql = "select name,age from class;"
cur.execute(sql)
# cur 游标是可迭代对象 ,通过迭代获取select效果
# for i in cur:
#     print(i)
#     print(i[0], i[1])

# cur.fetchone()获取第一个查询结果
# print(cur.fetchone())
# cur.fetchmany(n)获取前n个查询结果
# print(cur.fetchmany(3))
# cur.fetchall()获取所有查询结果
print(cur.fetchall())
# 关闭游标和数据库链接
db.commit()
cur.close()
db.close()
