import pymysql

f = open('dict.txt', 'rt')
while True:
    data = f.readline()
    if not data:
        break
    # data = data.strip()
    # data = data.split('  ')
    # while '' in data:
    #     for i in data:
    #         if i=='':
    #             data.remove(i)
    # print(data)
    data1 = data[:16]
    data2 = data[16:]
    data1 = data1.strip()
    data2 = data2.strip()

    # print(data1,'+++++',data2)
    db = pymysql.connect("localhost","root","7051","dict",charset="utf8")
    cur = db.cursor()       
    try:
        my_sqlyj = "insert into dict values('%s','%s');"%(data1, data2)
        cur.execute(my_sqlyj)
        print(my_sqlyj)
        db.commit()
    except:
        db.rollback()
        print('失败')
    db.close()



f.close()
