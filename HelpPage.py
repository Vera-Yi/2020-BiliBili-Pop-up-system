from tkinter import *
from PIL import ImageTk

class HelpFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self, height=1).pack()

        img1 = ImageTk.PhotoImage(file='help1.png')
        label_img1 = Label(self, image=img1)
        label_img1.image = img1
        label_img1.pack(side='top')

        Label(self, height=1).pack()

        img2 = ImageTk.PhotoImage(file='help2.png')
        label_img2 = Label(self, image=img2)
        label_img2.image = img2
        label_img2.pack(side='top')