from tkinter import *
from GetPage import *  # 菜单栏对应的各个子页面
from SendPage import *
from HelpPage import *


class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (1000, 650))  # 设置窗口大小
        self.createUpper()

    def createUpper(self):
        self.MainPage = MainFrame(self.root)  # 创建不同Frame
        self.GetPage = GetFrame(self.root)
        self.SendPage = SendFrame(self.root)
        self.HelpPage = HelpFrame(self.root)
        self.MainPage.pack()  # 默认显示主页


        menubar = Menu(self.root)
        menubar.add_command(label='主页', command=self.gotoMain)
        menubar.add_command(label='爬取弹幕信息', command=self.gotoGet)
        menubar.add_command(label='自动发送弹幕', command=self.gotoSend)
        menubar.add_command(label='使用须知', command=self.gotoHelp)
        self.root['menu'] = menubar  # 设置菜单栏

    def gotoMain(self):
        self.MainPage.pack()
        self.GetPage.pack_forget()
        self.SendPage.pack_forget()
        self.HelpPage.pack_forget()

    def gotoGet(self):
        self.MainPage.pack_forget()
        self.GetPage.pack()
        self.SendPage.pack_forget()
        self.HelpPage.pack_forget()

    def gotoSend(self):
        self.MainPage.pack_forget()
        self.GetPage.pack_forget()
        self.SendPage.pack()
        self.HelpPage.pack_forget()

    def gotoHelp(self):
        self.MainPage.pack_forget()
        self.GetPage.pack_forget()
        self.SendPage.pack_forget()
        self.HelpPage.pack()


class MainFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()


    def createPage(self):

        img = ImageTk.PhotoImage(file='t.jpg')
        label_img = Label(self, image=img)
        label_img.image = img
        label_img.pack(side='top')

        img2 = ImageTk.PhotoImage(file='b.png')
        label_img2 = Label(self, image=img2)
        label_img2.image = img2
        label_img2.pack(side='top')

        img3 = ImageTk.PhotoImage(file='title.png')
        label_img3 = Label(self, image=img3)
        label_img3.image = img3
        label_img3.pack(side='top')

        Label(self).pack()

        img4 = ImageTk.PhotoImage(file='sucess1.png')
        label_img4 = Label(self, image=img4)
        label_img4.image = img4
        label_img4.pack(side='top')

        img5 = ImageTk.PhotoImage(file='sucess2.png')
        label_img5 = Label(self, image=img5)
        label_img5.image = img5
        label_img5.pack(side='top')








