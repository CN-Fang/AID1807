from tkinter import *
from tkinter.messagebox import *
from time import *
from admin_table import admin_table


class menue_():
    def __init__(self, name, w, h):
        self.root = Tk()
        self.root.title(name)
        self.frame = Frame(self.root)
        self.width = w
        self.height = h
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height,
                                         (self.screenwidth-self.width)/2, (self.screenheight-self.height)/2)
        self.username = StringVar()
        self.password = StringVar()
        self.frame.pack()

        # 这里实现添加按钮
        self.createForm()

        self.root.geometry(self.alignstr)  # 居中对齐

        self.root.mainloop()

    # 添加按钮，标签组等
    def createForm(self):
        Label(self.frame).grid(row=0, stick=W, pady=10)
        Label(self.frame, text='账户：').grid(row=1,
                                           stick=W, pady=10)
        Entry(self.frame, textvariable=self.username).grid(
            row=1, column=1, stick=E)
        Label(self.frame, text='密码：').grid(row=2,
                                           stick=W, pady=10)
        Entry(self.frame, textvariable=self.password, show='*').grid(
            row=2, column=1, stick=E)


# 登录类
class entry_(menue_):
    def __init__(self):
        super().__init__('楼顶物流登录', 280, 200)
        self.createForm()

    def loginCheck(self):
        name = self.username.get().strip()
        secret = self.password.get().strip()

        mys = admin_table('admin_infor')
        result = mys.get_infor(name)
        print(result)
        if result != ():
            if result[0][2] == 'lock':
                if secret == result[0][1]:
                    print("登录成功")
                    showwarning(title='成功', message='登录成功')
                else:
                    result[0][3] += 1
                    update_infor([name, 'lock', result[0][3]])

                    if result[0][3] == 3:
                        self.update_infor([name, 'lock', 3])
                        showwarning(title='错误', message='您的账户已加锁请联系管理员')
                        return
                    showwarning(title='错误', message='密码错误，请确认后输入')
                    return
            else:
                showwarning(title='错误', message='您的账户已加锁请联系管理员')
                return
        else:
            showinfo(title='错误', message='用户名不存在，请确认后输入')
        self.frame.quit()

    def createForm(self):
        super().createForm()
        Button(self.frame, text='登录', command=self.loginCheck
               ).grid(row=3, stick=W, pady=10)
        Button(self.frame, text='退出', command=self.frame.quit
               ).grid(row=3, column=1, stick=E)


# 设置注册类
class resgis_(menue_):
    def __init__(self):
        super().__init__('楼顶物流注册', 500, 500)
        self.createForm()

    def createForm(self):
        super().createForm()
        self.emialstr = StringVar()
        self.numstr = StringVar()
        Label(self.frame, text='邮箱：').grid(row=3,
                                           stick=W, pady=10)
        Entry(self.frame, textvariable=self.emialstr).grid(
            row=3, column=1, stick=E)
        Label(self.frame, text='手机号：').grid(row=4,
                                            stick=W, pady=10)
        Entry(self.frame, textvariable=self.numstr).grid(
            row=4, column=1, stick=E)
        Button(self.frame, text='注册', command=self.register_login
               ).grid(row=5, column=1, stick=W)
        Button(self.frame, text='取消', command=self.frame.quit
               ).grid(row=5, column=1, stick=E)

    def register_login(self):
        mys = admin_table("admin_infor")
        name = self.username.get().strip()
        secret = self.password.get().strip()
        emialstr = self.emialstr.get().strip()
        numstr = self.numstr.get().strip()
        result = mys.get_infor(name)
        if not result:
            if not name:
                showwarning(title='错误', message='用户名不能为空')
                return False
            elif not secret:
                showwarning(title='错误', message='用密码不能为空')
                return False
            elif not emialstr:
                showwarning(title='错误', message='邮箱不能为空')
                return False
            elif not numstr:
                showwarning(title='错误', message='手机号不能为空')
                return False
            else:
                mys.set_infor(name, secret)
                showwarning(title='恭喜', message='账户注册成功')
        else:
            showwarning(title='错误', message='用户名已存在，请重新输入')
            return
        sleep(0.1)
        self.frame.quit()


if __name__ == "__main__":
    pa = resgis_()
