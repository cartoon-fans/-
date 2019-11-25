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
try:
    # insert 插入
    # sql = "insert into class (name,age,score) \
    # value ('Dave',16,92);" 写死

    # name = input("输入姓名")
    # age = input("输入年龄")
    # score = input("输入成绩")

    # sql = "insert into class (name,age,score) \
    # value ('%s',%s,%s);" % (name, age, score)

    # 使用execute 给sql传递参量
    # sql = "insert into class (name,age,score) \
    # value (%s,%s,%s);"
    # cur.execute(sql, [name, age, score])

    # update 操作
    # sql="update class set sex='m' where name = 'bill';"
    # cur.execute(sql)
    # delete 删除
    # sql = "delete from class  where sex is null ;"
    # cur.execute(sql)
    exe = []
    for i in range(3):
        name = input("输入姓名")
        age = input("输入年龄")
        score = input("输入成绩")
        exe.append((name, age, score))
    sql = "insert into class (name,age,score) \
    value (%s,%s,%s);"
    cur.executemany(sql, exe)
    db.commit()  # 同步写操作结果
except Exception as e:
    print(e)
    db.rollback()  # 出错时将数据库回滚到之前的状态
cur.close()
db.close()
