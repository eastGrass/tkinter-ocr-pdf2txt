from tkinter import *
win = Tk()
win.title(string="古诗鉴赏")
Label(win,text="山气日夕佳，飞鸟相与还。此中有真意，只是已忘言").pack()
Button(win,text="关闭",command=win.quit).pack(side="bottom")
win.mainloop()