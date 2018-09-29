from tkinter import *
from tkinter.messagebox import *
from time import *

from entry import menue_


# 表单类
class form_control(menue_):

    def __init__(self):
        super().__init__('楼顶物流－－订单列表', 850, 850)
        self.createForm()

    def createForm(self):
        self.formnum = StringVar()
        self.harvestername = StringVar()
        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        Label(self.frame).grid(row=0, stick=W, pady=10)
        Label(self.frame, text='订单号').grid(
            row=1, column=1, pady=10)
        Entry(self.frame, textvariable=self.formnum).grid(
            row=1, column=2)
        Label(self.frame, text='收件人'
              ).grid(row=1, column=3, pady=10
                     )
        Entry(self.frame, textvariable=self.harvestername).grid(
            row=1, column=4)
        Label(self.frame, text='订单状态').grid(
            row=1, column=5, pady=10)
        Entry(self.frame, textvariable='待确认').grid(
            row=1, column=6, pady=10)
        Label(self.frame, text='待确认　待付款　待发货').grid(row=1,
                                                   column=7, pady=10)
        C1 = Checkbutton(self.frame, text="订单号", variable=CheckVar1,
                         onvalue=1, offvalue=0).grid(row=2,column=1,pady=10)
        Label(self.frame, text='下单时间').grid(row=2, column=2, pady=10)
        Label(self.frame, text='收获人').grid(row=2, column=3, pady=10)
        Label(self.frame, text='总金额').grid(row=2, column=4, pady=10)
        Label(self.frame, text='应付金额').grid(row=2, column=5, pady=10)
        Label(self.frame, text='订单状态').grid(row=2, column=6, pady=10)
        Label(self.frame, text='操作').grid(row=2, column=7, pady=10)
        # C2 = Checkbutton(top, text = "GOOGLE", variable = CheckVar2, \
        #                  onvalue = 1, offvalue = 0, height=5, \
        #                  width = 20)
        # C1.pack()
        # C2.pack()

    # def onCheck(self):

    #     self.frame.quit()


if __name__ == "__main__":
    pa = form_control()
