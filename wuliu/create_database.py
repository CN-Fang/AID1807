from pymysql import connect

class MysqlHelp:
    def __init__(self,database,host="localhost",
                 user="root",password="123456",
                 charset="utf8",port=3306):
        self.database = database
        self.host = host
        self.user = user 
        self.password = password
        self.charset = charset
        self.port = port

    # 连接数据方法
    def open(self):
        # 创建conn
        self.conn = connect(host=self.host,
                user=self.user,password=self.password,
                database=self.database,
                charset=self.charset,
                port=self.port)
        # 创建游标cur
        self.cur = self.conn.cursor()

    # 关闭
    def close(self):
        self.cur.close()
        self.conn.close()

    # def get_infor(self, name):
    #     self.open()
    #     print(name)
    #     sql = "select name,password,lock_status,lock_num \
    #      from admin_infor where name = '%s';"%(name)
        
    #     self.cur.execute(sql)        
    #     print("ok")
    #     self.conn.commit()
    #     result = self.cur.fetchall()              
    #     self.close()
    #     return result
    #     # 插入记录
    # def set_infor(self, name, password, 
    #         lock_status = 'lock', lock_num = 0):
    #     self.open()
    #     sql = 'insert into admin_infor values("%s","%s","%s",%d);'%\
    #     (name, password, lock_status, lock_num)
    #     self.cur.execute(sql)
    #     self.conn.commit()

    #     print('ok')
    #     self.close()
    #     # 删除记录
    # def drop_infor(self, name):
    #     self.open()
    #     sql = 'delete from admin_infor where name = %s;'%name
    #     self.cur.execute(sql)
    #     print('ok')
    #     self.close()
    #     # 修改记录
    # def update_infor(self, L = {}):
    #     self.open()
    #     for s in L:
    #         sql = 'update admin_infor set %s = %s where %s = %s;'%\
    #         (s,s,s,s)
    #         self.cur.execute(sql)
    #     print('ok')
    #     self.close()
    # def entry_table(self, )




