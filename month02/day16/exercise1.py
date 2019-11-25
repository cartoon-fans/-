import pymysql


class Datebase:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='use_msg',
                                  charset='utf8')
        self.cur = self.db.cursor()

    def register(self, name, passwd):
        sql = "select name from msg where name ='%s';" % name
        self.cur.execute(sql)
        tup = self.cur.fetchone()
        if tup:
            return False
        try:
            sql = "insert into msg (name,password) \
            values(%s,%s);"
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(e)
            return False

    def login(self,name,passwd):
        sql = "select name,password from msg where name='%s'and password=%s;" % (name,passwd)
        self.cur.execute(sql)
        tup = self.cur.fetchone()
        if tup:
            return True
        else:
            return False
if __name__ == '__main__':
    db = Datebase()
    print(db.register("lil","123"))
    # print(db.login("lily","123"))

