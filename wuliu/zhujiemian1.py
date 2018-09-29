import tkinter as tk


def do_job():
    pass

def caidanlan():
    window = tk.Tk()
    window.title('楼上说的队物流管理系统')
    width = 1500
    height = 800
    #获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = window.winfo_screenwidth()  
    screenheight = window.winfo_screenheight() 
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
    window.geometry(alignstr)

    menubar = tk.Menu(window)

    menu1 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='客户管理', menu=menu1)

    menu1.add_command(label='客户基本信息管理', command=do_job)
    menu1.add_command(label='客户查询', command=do_job)

    # filemenu.add_separator()

    # filemenu.add_command(label='Exit', command=window.quit)

    menu2 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='订单管理', menu=menu2)

    menu2.add_command(label='订单受理', command=do_job)
    menu2.add_command(label='订单输入', command=do_job)
    menu2.add_command(label='订单类型', command=do_job)
    menu2.add_command(label='订单分配', command=do_job)
    menu2.add_command(label='订单查询', command=do_job)
    menu2.add_command(label='订单确认', command=do_job)
    menu2.add_command(label='订单打印', command=do_job)


    menu3 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='收货管理', menu=menu3)

    menu3.add_command(label='入库类型', command=do_job)
    menu3.add_command(label='入库方式', command=do_job)
    menu3.add_command(label='货物验收', command=do_job)
    menu3.add_command(label='收货单打印', command=do_job)
    menu3.add_command(label='库位分配', command=do_job)
    menu3.add_command(label='库位清单打印', command=do_job)
    menu3.add_command(label='预入库确认', command=do_job)
    menu3.add_command(label='直接入库处理', command=do_job)

    menu4 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='出货管理', menu=menu4)

    menu4.add_command(label='出库类型', command=do_job)
    menu4.add_command(label='拣货清单打印', command=do_job)
    menu4.add_command(label='拣货处理', command=do_job)
    menu4.add_command(label='预出库调整', command=do_job)
    menu4.add_command(label='预出库确认', command=do_job)
    menu4.add_command(label='直接出库处理', command=do_job)
    menu4.add_command(label='送货单打印', command=do_job)

    menu5 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='配送管理和车辆管理', menu=menu5)

    menu5.add_command(label='配送管理', command=do_job)
    menu5.add_command(label='车辆管理', command=do_job)

    menu6 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='货物管理', menu=menu6)   

    menu6.add_command(label='库存查询', command=do_job)

    menu7 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='库存管理', menu=menu7) 

    menu7.add_command(label='调整处理', command=do_job)
    menu7.add_command(label='内拨处理', command=do_job)
    menu7.add_command(label='盘点处理', command=do_job)
    menu7.add_command(label='退货处理', command=do_job)
    menu7.add_command(label='调换处理', command=do_job)
    menu7.add_command(label='包装处理', command=do_job)
    menu7.add_command(label='报废处理', command=do_job)
    menu7.add_command(label='库存台帐', command=do_job)

    menu8 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='财务结算', menu=menu8) 

    menu8.add_command(label='运输费确认', command=do_job)
    menu8.add_command(label='收款处理', command=do_job)
    menu8.add_command(label='付款处理', command=do_job)
    menu8.add_command(label='收款查询', command=do_job)
    menu8.add_command(label='付款查询', command=do_job)
    menu8.add_command(label='应收款查询', command=do_job)
    menu8.add_command(label='应付款查询', command=do_job)
    menu8.add_command(label='销应收款查询', command=do_job)
    menu8.add_command(label='销应付款查询', command=do_job)

    menu9 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='基本信息维护', menu=menu9)

    menu9.add_command(label='基本信息维护', command=do_job)

    menu10 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='系统管理', menu=menu10)

    menu10.add_command(label='系统管理', command=do_job)


    window.config(menu=menubar)

    window.mainloop()

if __name__ == '__main__':
    caidanlan()