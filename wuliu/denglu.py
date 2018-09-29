import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pymysql
from time import sleep


def denglu():
    window = tk.Tk()
    window.title('楼上说的队物流管理系统')
    window.geometry('450x300')

    # welcome image
    canvas = tk.Canvas(window, height=450, width=500)
    image_file1 = tk.PhotoImage(file='beijing.gif')
    image1 = canvas.create_image(0, 0, anchor='nw', image=image_file1)
    image_file = tk.PhotoImage(file='welcome.png')
    image = canvas.create_image(80, 20, anchor='nw', image=image_file)
    canvas.pack()


    # user information
    tk.Label(window, text='用户名: ').place(x=70, y=100)
    tk.Label(window, text='密码: ').place(x=70, y=170)
    var_usr_name = tk.StringVar()
    var_usr_name.set('admin')
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
    entry_usr_name.place(x=160, y=100)
    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
    entry_usr_pwd.place(x=160, y=170)


    def usr_login():
        db = pymysql.connect("localhost","root","7051",
                     "lou",charset="utf8")
        cur = db.cursor()       
        sql_select = "select * from user;"
        cur.execute(sql_select)

        data = cur.fetchall()
        db.close()
        

        for i in data:
            print(i)
            usr_name = var_usr_name.get()
            usr_pwd = var_usr_pwd.get()
            if usr_name == i[0]:
                if usr_pwd == i[1]:
                    tk.messagebox.showinfo(title='登录成功', message='欢迎您! ' + usr_name)
                    # zhujiemian()
                    # window.destroy()
                    break

                else:
                    tk.messagebox.showerror(message='密码输入错误,请重试!')
                    break
        else:
            is_sign_up = tk.messagebox.askyesno('Welcome','该用户名不存在,是否注册?')

            if is_sign_up:

                usr_sign_up()

    def usr_sign_up():
        def sign_to():
            np = new_pwd.get()
            npf = new_pwd_confirm.get()
            nn = new_name.get()

            db = pymysql.connect("localhost","root","7051","lou",charset="utf8")
            cursor = db.cursor()

            sql_selct = 'select * from user;'
            cursor.execute(sql_selct)
            data = cursor.fetchall()

            for i in data:
                if nn == i[0]:
                    tk.messagebox.showerror('Error', '该用户名已存在!')
                    break
            else:
                if np == '':  
                    tk.messagebox.showerror(
                            'Error', '密码不能为空!')  
                elif np != npf:
                    tk.messagebox.showerror(
                        'Error', '两次密码必须一致!')                    
                else:
                    try:
                        my_sqlyj = "insert into user values('%s','%s');"%(nn, np)
                        cursor.execute(my_sqlyj)
                        print(my_sqlyj)
                        db.commit()
                    except:
                        db.rollback()
                    db.close()

                    tk.messagebox.showinfo(
                        'Welcome', '您已注册成功!')
                    window_sign_up.destroy()

        window_sign_up = tk.Toplevel(window)
        window_sign_up.geometry('350x200')
        window_sign_up.title('Sign up window')

        new_name = tk.StringVar()

        tk.Label(window_sign_up, text='用户名: ').place(x=10, y=10)
        entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
        entry_new_name.place(x=150, y=10)
        new_pwd = tk.StringVar()

        tk.Label(window_sign_up, text='密码: ').place(x=10, y=50)
        entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.place(x=150, y=50)
        new_pwd_confirm = tk.StringVar()

        tk.Label(window_sign_up, text='请重复密码: ').place(x=10, y=90)
        entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_confirm.place(x=150, y=90)
        btn_comfirm_sign_up = tk.Button(window_sign_up, text='注册', command=sign_to)
        btn_comfirm_sign_up.place(x=150, y=130)


    # login and sign up button


    btn_login = tk.Button(window, text='登录', command=usr_login)
    btn_login.place(x=120, y=230)
    btn_sign_up = tk.Button(window, text='注册', command=usr_sign_up)
    btn_sign_up.place(x=270, y=230)

    sleep(0.1)
    window.mainloop()

if __name__ == '__main__':
    denglu()
