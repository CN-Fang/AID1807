import sys, os
import pymysql
#  mysql -hxdm458352141.my3w.com:3306 -uxdm458352141 -p13920331770.Pg
# 
def denglu():
        name = input('请输入用户名：')
        password = input('请输入密码：')
        db = pymysql.connect("localhost","root","7051",
                     "dict",charset="utf8")
        cur = db.cursor()       
        sql_select = "select * from user;"
        cur.execute(sql_select)

        data = cur.fetchall()
        db.close()
        

        for i in data:
            # print(i)

            if name == i[1]:
                if password == i[2]:
                    print('登录成功！欢迎您', name)
                    break
                else:
                    print('密码输入错误，请重试！')
                    break
        else:
            a = input('该用户名不存在，是否注册？（y/n）')
            if a == "y":
                zhuce()
            elif a == "n":
                denglujiemian()
            else:
                print('输入错误')


def zhuce():
        nn = input('请输入用户名：')
        np = input('请输入密码：')

        db = pymysql.connect("localhost","root","7051","dict",charset="utf8")
        cursor = db.cursor()

        sql_selct = 'select * from user;'
        cursor.execute(sql_selct)
        data = cursor.fetchall()

        for i in data:
            if nn == i[1]:
                print('该用户名已存在！')
                break
        else:
            if np == '':  
                print('密码不能为空!')  
                    
            else:
                try:
                    my_sqlyj = "insert into user (name,password) values('%s','%s');"%(nn, np)
                    cursor.execute(my_sqlyj)
                    print(my_sqlyj)
                    db.commit()
                except:
                    db.rollback()
                db.close()

                print('您已注册成功!')
                denglujiemian()

    
def denglujiemian():
    while True:
        print('+--------------------+')
        print('+-------1登录--------+')
        print('+-------2注册--------+')
        print('+-------3退出--------+')
        print('+--------------------+')
        a = input('请输入选项：')
        if a == "1":
            denglu()
        elif a == "2":
            zhuce()
        elif a == "3":
            sys.exit(0)
        else:
            print('输入错误，请重试')
            continue

# denglujiemian()