from create_database import MysqlHelp


class admin_table(MysqlHelp):

    def __init__(self, table_name):
        self.table_name = table_name
        super().__init__("mangement")

    def get_infor(self, name):
        self.open()
        print(name)
        sql = "select name,password,lock_status,lock_num \
         from %s where name = '%s';" % (self.table_name, name)

        self.cur.execute(sql)
        # print("ok")
        self.conn.commit()
        result = self.cur.fetchall()
        self.close()
        return result
        # 插入记录

    def set_infor(self, name, password,
                  lock_status='lock', lock_num=0):
        self.open()
        sql = 'insert into %s values("%s","%s","%s",%d);' %\
            (self.table_name, name, password, lock_status, lock_num)
        self.cur.execute(sql)
        self.conn.commit()

        print('ok')
        self.close()
        # 删除记录

    def drop_infor(self, name):
        self.open()
        sql = 'delete from %s where name = %s;' % (self.table_name, name)
        self.cur.execute(sql)
        self.conn.commit()
        print('ok')
        self.close()
        # 修改记录

    def update_infor(self, L=[]):
        self.open()
        sql = 'update %s set lock_status = %s, lock_num = \
        %d where name = %s;' % (self.table_name, L[1], L[2], L[0])
        self.cur.execute(sql)
        print('ok')
        self.conn.commit()
        self.close()

