from tkinter import *
from PIL import ImageTk
import requests
import re
import jieba
import wordcloud
import os

class GetFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        self.t = StringVar()
        self.t.set("例:177974677")
        ll = ImageTk.PhotoImage(file='p1.jpg')
        label_ll = Label(self, image=ll)
        label_ll.image = ll
        label_ll.pack(side='left', anchor='nw', ipadx=10, ipady=30)

        rr = ImageTk.PhotoImage(file='p2.jpg')
        label_rr = Label(self, image=rr)
        label_rr.image = rr
        label_rr.pack(side='right', anchor='ne', ipadx=10, ipady=30)

        img = ImageTk.PhotoImage(file='b.png')
        label_img = Label(self, image=img)
        label_img.image = img
        label_img.pack(side='top')

        f1 = Frame(self)
        f1.pack()

        Label(f1, text='请输入要爬取的视频id：').pack(side='left')
        Entry(f1, textvariable=self.t, width=15).pack(side='left')
        Label(f1, width=1).pack(side='left')
        Button(f1, text='开始爬取', command=self.confirm).pack(side='left')

        self.sh1 = StringVar()
        show1 = Label(self, text='=========', textvariable=self.sh1,fg='#00CCFF')
        show1.pack()

        Button(self, text='显示图片', command=self.show_image).pack()
        Label(self, height=1).pack()


    def confirm(self):
        self.sh1.set("请输入正确的B站视频号")
        aid = self.t.get()

        def get_danmu(url):
            response = requests.get(url, headers)
            response = response.content.decode('utf-8')
            print(response)
            # 通过正则表达式获取两个<d>标签内包含的弹幕信息
            data = re.compile('<d.*?>(.*?)</d>')
            # 对目标网页使用正则表达式，获取所有匹配的内容
            danmu = data.findall(response)
            danmu_word = jieba.lcut(" ".join(danmu))
            danmu_str = " ".join(danmu_word)
            w = wordcloud.WordCloud(font_path="msyh.ttc", background_color='white', width=1000, height=500)
            w.generate(danmu_str)
            w.to_file('danmu.png')

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

        s = aid
        # 例如：41551729/177974677
        s = "https://api.bilibili.com/x/v1/dm/list.so?oid=" + s
        # 将用户输入的弹幕地址去掉空格并加载到get_danmu()中
        get_danmu(s.strip())

        if (os.path.exists('danmu.png') == True):
            self.sh1.set("弹幕词云生成成功，图片已保存到本地，点击下方按钮查看图片")
        else:
            self.sh1.set("生成失败，请稍后重试")
    def back(self):
        self.page.destroy()

    def show_image(self):
        photo = ImageTk.PhotoImage(file='danmu.png')
        P1 = Label(self, image=photo, height=400, width=800)
        P1.image = photo
        P1.pack(side='top')







