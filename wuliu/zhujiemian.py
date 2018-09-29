import tkinter as tk


# 客户管理
def kehuguanli():
    pass

# 订单管理
def dingdanguanli():
    pass

# 收货管理
def shouhuoguanli():
    pass

# 出库管理
def chukuguanli():
    pass

# 配送管理和车辆管理
def peisongguanli():
    pass

# 货物管理
def huowuguanli():
    pass

# 库存管理
def kucunguanli():
    pass

# 财务结算
def caiwujiesuan():
    pass

# 基本信息维护
def jibenxinxi():
    pass

# 系统管理
def xitongguanli():
    pass

# 主界面
def zhujiemian():
    window = tk.Tk()
    window.title('主界面')
    window.geometry('1200x700')
    window.resizable(width=False, height=False)
    window.attributes("-alpha", 0)

    canvas = tk.Canvas(window, height=700, width=1200)
    image_file = tk.PhotoImage(file = 'beijing3.png')
    image = canvas.create_image(0, 0, anchor='center', image=image_file)
    canvas.pack()

    image_file1 = tk.PhotoImage(file = '客户管理.png')
    btn_login = tk.Button(window, width=201, height=149, image = image_file1, command=kehuguanli)
    btn_login.place(x=100, y=230)
    # btn_sign_up = tk.Button(window, text="订单管理", width=15, height=7, command=dingdanguanli)
    # btn_sign_up.place(x=250, y=230)
    btn_sign_up = tk.Button(window, text="收货管理", width=15, height=7, command=shouhuoguanli)
    btn_sign_up.place(x=400, y=230)
    btn_sign_up = tk.Button(window, text="出货管理", width=15, height=7, command=chukuguanli)
    btn_sign_up.place(x=550, y=230)
    btn_sign_up = tk.Button(window, text="配送管理和车辆管理", width=15, height=7, command=peisongguanli)
    btn_sign_up.place(x=700, y=230)
    btn_sign_up = tk.Button(window, text="库存管理", width=15, height=7, command=kucunguanli)
    btn_sign_up.place(x=100, y=500)
    btn_sign_up = tk.Button(window, text="财务结算", width=15, height=7, command=caiwujiesuan)
    btn_sign_up.place(x=250, y=500)
    btn_sign_up = tk.Button(window, text="基本信息维护", width=15, height=7, command=jibenxinxi)
    btn_sign_up.place(x=400, y=500)
    btn_sign_up = tk.Button(window, text="系统管理", width=15, height=7, command=xitongguanli)
    btn_sign_up.place(x=550, y=500)




    window.mainloop()

if __name__ == '__main__':
    zhujiemian()