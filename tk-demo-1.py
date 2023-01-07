import tkinter as tk
import tkinter.filedialog
import tkinter.ttk
import tkinter.messagebox
import pdf2txt_demo_1 

class OcrTkGgi(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.title("OCR or Quality")
        self.geometry('700x150')  # 设置窗口大小
        # self.attributes("-toolwindow", 2) # 标题栏无最大化，最小化

        # tkinter var
        self.strInFilePath = tk.StringVar()
        self.strOutDir = tk.StringVar()
        self.strConfigFilePath = tk.StringVar()

        # in file column
        labelIn = tk.Label(self, width=15, text="Input file:")
        entryIn = tk.Entry(self, width=60, textvar=self.strInFilePath)
        btnOpenInFile = tk.Button(self, text="Open File", width=15, command=self.onFileDlg)

        labelIn.grid(row=0, sticky=tk.W)
        entryIn.grid(row=0, column=1,columnspan=3)
        btnOpenInFile.grid(row=0, column=4)

        # out file column
        labelOut = tk.Label(self, width=15,text="Output Dir:")
        entryOutDir = tk.Entry(self, width=60, textvar=self.strOutDir)
        btnOpenOutDir = tk.Button(self, text="Open out Dir", width=15, command=self.onOutDirDlg)

        labelOut.grid(row=1, sticky=tk.W)
        entryOutDir.grid(row=1, column=1,columnspan=3)
        btnOpenOutDir.grid(row=1, column=4)

        # configure
        labelConfig = tk.Label(self, width=15,text="OCR configure:")
        entryConfig = tk.Entry(self, width=60, textvar=self.strConfigFilePath)
        # entry默认值
        entryConfig.insert(0, r"D:\Program Files\Tesseract-OCR\tesseract.exe")
        btnConfigDir = tk.Button(self, text="OCR config", width=15, command=self.onConfigDlg)

        labelConfig.grid(row=2, sticky=tk.W)
        entryConfig.grid(row=2, column=1,columnspan=3)
        btnConfigDir.grid(row=2, column=4)

        # button column
        btnCancel = tk.Button(self, text="Cancel", width=15, command=self.onCancel)

        btnOcr = tk.Button(self, text="OCR", width=15, command=self.onOcr)
        btnQuality = tk.Button(self, text="Quality", width=15, command=self.onQuality)

        btnCancel.grid(row=3, column=1, sticky=tk.E)
        btnOcr.grid(row=3, column=2)
        btnQuality.grid(row=3, column=3, sticky=tk.W)

        # progressbar
        progressbarOcr = tk.ttk.Progressbar(self,length=500)
        progressbarOcr.grid(row=4, column=1, columnspan=4)

        # 进度值最大值
        progressbarOcr['maximum'] = 100
        # 进度值初始值
        progressbarOcr['value'] = 0

    def onFileDlg(self):
        # 文件选择框
        filePath = tkinter.filedialog.askopenfilename()

        if (filePath != ''):
            self.strInFilePath.set(filePath)
        else:
            tkinter.messagebox.askokcancel("Quit", "no pdf file?")

    def onOutDirDlg(self):
        # 选择文件夹
        folderPath = tkinter.filedialog.askdirectory()

        if (folderPath != ''):
            self.strOutDir.set(folderPath)

    def onConfigDlg(self):
        # 文件选择框
        filePath = tkinter.filedialog.askopenfilename()

        if (filePath != ''):
            self.strConfigFilePath.set(filePath)
        else:
            tkinter.messagebox.askokcancel("Quit", "no orc engine?")


    def onCancel(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

    def onOcr(self):
        print("in = {0}, out = {1}, config={2}".format( \
            self.strInFilePath.get(), \
            self.strOutDir.get(), \
            self.strConfigFilePath.get()))
        pdf2txt_demo_1.pdf2txt_demo(self.strInFilePath.get(), \
            self.strOutDir.get(),self.strConfigFilePath.get())

    def onQuality(self):
        pass


if __name__ == "__main__":
    window = OcrTkGgi()
    window.mainloop()