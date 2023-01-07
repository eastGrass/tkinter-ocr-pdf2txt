import time
import tkinter
import tkinter.ttk


def show():
    # 进度值最大值
    progressbarOne['maximum'] = 100
    # 进度值初始值
    progressbarOne['value'] = 0
    for i in range(100):
        time.sleep(0.5)
        progressbarOne['value'] += 1
        root.update()

root = tkinter.Tk()
root.geometry('150x120')

progressbarOne = tkinter.ttk.Progressbar(root)
progressbarOne.pack(side=tkinter.TOP)

confirm_button=tkinter.Button(root,text="确定",command=show)
confirm_button.pack(side=tkinter.TOP)
root.mainloop()