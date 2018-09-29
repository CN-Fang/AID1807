import pymysql
import re


f = open('dict.txt')
db = pymysql.connect('localhost', 'root', '123456', 'dict')
cursor = db.cursor()

for line in f:
    l = re.split(r'\s+', line)
    word = l[0]
    interpret = ' '.join(l[1:])
    sql = 'insert into dict (word, jieshi) values("%s","%s")'%(word, interpret)

    try:
        cursor.execute(sql)
        db.commit()
        print('成功')
    except:
        db.rollback()
        print('失败')
f.close()