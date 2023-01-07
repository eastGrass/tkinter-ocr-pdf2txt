#设置Label控件颜色
from tkinter import *
win = Tk() 
win. title (string ="古诗鉴赏")
Label (win, background="#00ff00", text="两个黄鹏鸣翠柳，一行白鹭上青天。").pack ()
Label (win, background="SystemHighlight", text="窗含西岭千秋雪，泊东吴万里船。").pack()
win.mainloop()