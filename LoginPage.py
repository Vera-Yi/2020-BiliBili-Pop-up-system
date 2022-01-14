from MainPage import *

class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (1000, 650))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()

        img = ImageTk.PhotoImage(file='t.jpg')
        label_img = Label(self.page, image=img)
        label_img.image = img
        label_img.pack(side='top')

        img2 = ImageTk.PhotoImage(file='b.png')
        label_img2 = Label(self.page, image=img2)
        label_img2.image = img2
        label_img2.pack(side='top')

        img3 = ImageTk.PhotoImage(file='title.png')
        label_img3 = Label(self.page, image=img3)
        label_img3.image = img3
        label_img3.pack(side='top')

        Label(self.page,height=3).pack()
        Button(self.page, text='开始', width=15,command=self.kaishi).pack()
        Label(self.page).pack()
        Button(self.page, text='退出', width=15, command=self.page.quit).pack()

    def kaishi(self):
        self.page.destroy()
        MainPage(self.root)




