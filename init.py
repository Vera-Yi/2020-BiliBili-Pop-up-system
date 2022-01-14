from tkinter import *
from LoginPage import *
import PIL
import requests
from re import *
import jieba
from wordcloud import *
from os import *
from time import *

root = Tk()
root.title('B站弹幕操作系统')
LoginPage(root)
root.mainloop()