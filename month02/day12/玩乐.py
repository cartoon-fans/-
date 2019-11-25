# from socket import *
#
# s = socket()
# # s.bind(('172.40.74.189', 8888))
#
# s.connect(('127.0.0.1', 8888))
# while True:
#     n = input("请输入")
#     s.send(n.encode())
#     data = s.recv(1024).decode()
#     print(data)

# import pymysql
#
# db = pymysql.connect(host='localhost', port=3306, user='root', password="123456", database='books', charset='utf8')
#
# cur = db.cursor()
#
# sql = "insert into index_test (name) values (%s);"
# exe = []
# s = "Tom"
# for i in range(2000000):
#     name = s + str(i)
#     exe.append(name)
#
# try:
#     cur.executemany(sql, exe)
#     db.commit()
# except:
#     db.rollback()
#
# db.close()
