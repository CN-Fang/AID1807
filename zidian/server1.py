import os, time, signal, pymysql, sys
from socket import *

# 定义需要的全局变量
DICT_TEXT = './dict.txt'
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)

# 流程控制
def main():
    # 创建数据库连接
    db = pymysql.connect('127.0.0.1', 'root', '123456', 'dict')

    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    # 忽略子进程信号
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        try:
            c, addr = s.accept()
            print("Connect from ", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue
            
        # 创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            do_child(c, db)
        else:
            c.close()
            continue

def do_child(c, db):
    # 循环接受客户端请求
    while True:
        data = c.recv(128).decode()
        print(c.getpeername(), ":", data)
        if (not data) or data[0] == 'E':
            c.close()
            sys.exit(0)
        elif data[0] == 'R':
            do_register(c, db, data)
        elif data[0] == 'L':
            do_login(c, db, data)
        elif data[0] == "Q":
            do_query(c, db, data)
        elif data[0] == "H":
            do_hist(c, db, data)

def do_login(c, db, data):
    print('登录操作')
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql = "select * from user where \
    name = '%s' and password = '%s'"%(name, passwd)
    cursor.execute(sql)
    r = cursor.fetchone()

    if r == None:
        c.send(b'FALL')
    else:
        print("%s登录成功"%name)
        c.send(b'OK')


def do_register(c, db, data):
    print('注册操作')
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()
    cursor.execute('select * from user where name = "%s"'%name)
    r = cursor.fetchone()
    if r != None:
        c.send(b'EXISTS')
        return

    # 插入用户数据
    try:
        cursor.execute('insert into user (name, password) values ("%s", "%s")'%(name, passwd))
        db.commit()
        c.send(b'OK')
    except:
        db.rollback()
        c.send(b'FALL')
    else:
        print("%s注册成功"%name)



def do_query(c, db, data):
    print('查询操作')
    l = data.split(' ')
    name = l[1]
    word = l[2]
    cursor = db.cursor()
    # 数据库查询,(有错)
    # cursor.execute('select jieshi from dict where word="%s"'%word)
    # r = cursor.fetchone()
    # c.send(b"OK")
    # c.send(r[0].encode())
    def insert_history():
        tm = time.ctime()
        sql = 'insert into history (name, word, time) \
        values("%s","%s","%s")'%(name, word, tm)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback
    # 文本查询
    try:
        f = open(DICT_TEXT)
    except:
        c.send(b"meidakai")
        return
    for line in f:
        tmp = line.split(' ')[0]
        if tmp > word:
            c.send(b"chaguole")
            f.close()
            return
        elif tmp == word:
            c.send(b'OK')
            time.sleep(0.1)
            c.send(line.encode())
            f.close()
            insert_history()
            return
    c.send(b"chawanle")
    f.close()


def do_hist(c, db, data):
    print('历史操作')
    l = data.split(' ')
    name = l[1]
    cursor = db.cursor()

    sql = "select * from history where name='%s'"%name
    cursor.execute(sql)
    r = cursor.fetchall()
    if not r:
        c.send(b'meilishi')
        return
    else:
        c.send(b'OK')
    for i in r:
        time.sleep(0.1)
        msg = "%s  %s  %s"%(i[1], i[2], i[3])
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b'##')





    
if __name__ == "__main__":
    main()