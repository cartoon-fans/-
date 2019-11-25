import hashlib

import pymysql


def change_passwd(passwd):
    salt = '*#06#'
    hash = hashlib.md5()
    hash.update(passwd.encode())
    passwd = hash.hexdigest()
    return passwd


class Datebase:
    def __init__(self, host='localhost', port=3306, user=None, password=None, database='dict', charset='utf8'):
        self.db = pymysql.connect(host=host,
                                  port=port,
                                  user=user,
                                  password=password,
                                  database=database,
                                  charset=charset)
        self.cur = None

    def create_cur(self):
        self.cur = self.db.cursor()

    def close(self):
        if self.cur:
            self.cur.close()
        self.db.close()

    def register(self, name, passwd):
        sql = "select name from user where name ='%s';" % name
        self.cur.execute(sql)
        tup = self.cur.fetchone()
        if tup:
            return False
        passwd = change_passwd(passwd)
        try:
            sql = "insert into user (name,passwd) values(%s,%s);"
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(e)
            return False

    def login(self, name, passwd):
        passwd = change_passwd(passwd)
        sql = "select name,passwd from user where name = %s and passwd = %s;"
        self.cur.execute(sql, [name, passwd])
        tup = self.cur.fetchone()
        if tup:
            return True
        else:
            return False

    def query(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        r = self.cur.fetchone()
        if r:
            return r[0]

    def insert_history(self, name, word):
        sql = "insert into his1 (name,word) values (%s,%s);"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except:
            self.db.rollback()

    def note(self, name):
        sql = "select name,word,time from his1 where name=%s order by time desc ; "
        self.cur.execute(sql, [name])
        return self.cur.fetchmany(10)
