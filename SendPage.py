from tkinter import *
from PIL import ImageTk
import requests
import time


show_list = []


class SendFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):

        self.room_temp = StringVar()
        self.room_temp.set("例:13686945")
        self.content_temp = StringVar()
        self.content_temp.set("Bilibili干杯╰(*°▽°*)╯")
        self.show_temp = StringVar()
        self.condition_temp = StringVar()

        ll = ImageTk.PhotoImage(file='p1.jpg')
        label_ll = Label(self, image=ll)
        label_ll.image = ll
        label_ll.pack(side='left', anchor='nw', ipadx=50, ipady=30)

        rr = ImageTk.PhotoImage(file='p2.jpg')
        label_rr = Label(self, image=rr)
        label_rr.image = rr
        label_rr.pack(side='right', anchor='ne', ipadx=50, ipady=30)

        img = ImageTk.PhotoImage(file='b.png')
        label_img = Label(self, image=img)
        label_img.image = img
        label_img.pack(side='top')

        f1 = Frame(self)
        f1.pack()
        Label(self).pack()
        f2 = Frame(self)
        f2.pack()

        Label(f1, text='请输入要发送弹幕的直播间房间号:').pack(side='left')
        Label(f1, width=1).pack(side='left')
        Entry(f1, textvariable=self.room_temp, width=15).pack(side='left')

        Label(f2, text='请输入要发送弹幕的弹幕内容:').pack(side='left')
        Label(f2, width=1).pack(side='left')
        Entry(f2, textvariable=self.content_temp, width=15).pack(side='left')
        Label(f2, width=1).pack(side='left')
        Button(f2, text='添加', command=self.fun_add).pack(side='left')

        Label(self,height=1).pack()
        Label(self, text='↓↓↓待发送的弹幕列表↓↓↓',fg='#00CCFF').pack()
        Label(self).pack()
        show1 = Label(self,width=120,height=3,bg='white',textvariable=self.show_temp)
        show1.pack()

        Label(self).pack()
        Button(self, text='确认发送', command=self.fun_send).pack()
        Label(self).pack()
        condition = Label(self,textvariable=self.condition_temp,fg='#00CCFF')
        condition.pack()


    def fun_add(self):
        show_word = self.content_temp.get()
        show_list.append(show_word)
        print(show_list)

        self.show_temp.set(show_list)

    def fun_send(self):
        room_id = self.room_temp.get()
        msg = show_list
        url = 'https://api.live.bilibili.com/msg/send'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
            "Cookie": "l=v; buvid3=22EA05DB-A44E-4E37-AAED-F3E1ED6324FA84598infoc; fts=1548413611; rpdid=|(u))|Y~)R~u0J'ullY~J||~m; _uuid=93E5D94A-6464-4B35-C7D0-BEACF0A4A2C935134infoc; LIVE_BUVID=b66f38f52563dc8dc57de52da456e3e1; LIVE_BUVID__ckMd5=9087f6ca59e89c1c; pgv_pvi=2990420992; _qddaz=QD.5y1jzj.ovyhyt.k1lt45n3; stardustvideo=1; laboratory=1-1; im_notify_type_362407411=0; DedeUserID=362407411; DedeUserID__ckMd5=bbde94af6224f8a0; SESSDATA=d32729e7%2C1600603083%2Ca6326*31; bili_jct=0cf721024e5008acea4032f4a371b2b3; CURRENT_QUALITY=116; CURRENT_FNVAL=16; sid=5gt5kvp0; PVID=3"
        }

        def messager(msg, room_id):
            data = {
                'color': '16777215',
                'fontsize': '25',
                'mode': '1',
                'msg': msg,
                'rnd': '1592473260',
                'roomid': room_id,
                'bubble': '0',
                'csrf_token': '0cf721024e5008acea4032f4a371b2b3',
                'csrf': '0cf721024e5008acea4032f4a371b2b3'
            }
            return data

        for i in msg:
            data = messager(i,room_id)
            text = requests.post(url, data=data, headers=headers).text
            print(i)
            time.sleep(1)
            print(text)

        info = 0
        rule = re.compile('.*?"code":0.*?')
        info = rule.findall(text)
        if info==0:
            self.condition_temp.set("发送失败，请确认该房间目前是否正在直播")
        else:
            self.condition_temp.set("发送成功，快去直播间看看吧！")
