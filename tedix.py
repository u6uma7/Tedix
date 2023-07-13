import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import sys
import webbrowser
import _thread


open_file_path = "cache_\\000.txt"

def my_message_box(title1, message1):
    win001 = tk.Toplevel()
    win001.title(title1)
    win001.geometry("300x225")
    message1 = "123"*1000
    if len(message1) > 255:
        message1 = message1[0:256]
    tk.Message(win001, text=message1).pack()
    tk.Button(win001, text="确定", command=win001.destroy).place(relx=0.0, rely=0.8, relheight=0.2, relwidth=1.0)
    win001.resizable(False, False)

def open_buy_web(event):
    webbrowser.open("https://tedix.rth1.one/buy", new=0)

def win2_help():
    win2 = tk.Toplevel()
    win2.geometry("400x300")
    win2.resizable(False, False)
    # tk.Label(win2, image=tk.PhotoImage(file="tedix.gif")).pack() 不知道为什么不能显示图片
    tk.Label(win2, text="Tedix v0.1.0").pack()
    tk.Label(win2, text="一个简单的文本编辑器").pack()
    tk.Label(win2, text="作者: Joulier429").pack()
    tk.Button(win2, text="确定", command=win2.destroy).place(relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1)

def sign_up_tedix():
    def nothing_like_that():
        win4 = tk.Toplevel()
        a = license_text_area.get("1.0", "end")
        a = a[0:-1]
        if a != "":
            b = "没有像那样东西😡"
        else:
            b = "这是我们信任的问题😡"
        win4.title(b)
        win4.geometry("300x100")
        tk.Label(win4, text=b).pack()
        tk.Button(win4, text="确定", command=win4.destroy).pack()
        win4.resizable(False, False)
    win3 = tk.Toplevel()
    win3.geometry("400x300")
    win3.title("输入注册码")
    win3.resizable(False, False)
    tk.Label(win3, text="请在请在下面输入您的密钥，").pack()
    url = tk.Label(win3, text="您可以在 https://tedix.rth1.one/buy 购买", fg="#1D6A96")
    url.pack()
    url.bind("<Button-1>", open_buy_web)
    license_text_area = tk.Text(win3)
    license_text_area.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.7)
    tk.Button(win3, text="确定", command=nothing_like_that).place(relx=0.3, rely=0.87, relheight=0.1, relwidth=0.4)

def saveas_file():
    global open_file_path
    saveas_path = tkinter.filedialog.asksaveasfilename(title="[ファイルとして保存]を選択してください")
    if saveas_path == "":
        tkinter.messagebox.showinfo("害tm带着那眼镜呢？文件那？", "我问你文件内，我文件呐？我文件啊啊啊啊啊！！！！！")
    else:
        with open(saveas_path, mode="w", encoding="utf-8") as file1:
            file1.write(textarea.get("1.0", "end"))
            open_file_path = saveas_path

def open_file(): # 打开文件
    global open_file_path
    def did_you_save_the_file():
        if open_file_path == "cache_\\000.txt":
            a_very_important_choice = tkinter.messagebox.askquestion("文件未保存", "要在保存文件之后打开文件吗")
            if a_very_important_choice:
                saveas_path = tkinter.filedialog.asksaveasfilename(title="[ファイルとして保存]を選択してください")
            if saveas_path == "":
                tkinter.messagebox.showinfo("害tm带着那眼镜呢？文件那？", "我问你文件内，我文件呐？我文件啊啊啊啊啊！！！！！")
            else:
                with open(saveas_path, mode="w", encoding="utf-8") as file1:
                    file1.write(textarea.get("1.0", "end"))
        else:
            with open(save_the_file) as file1:
                if file1 != textarea.get("1.0", "end"):
                    a_very_important_choice = tkinter.messagebox.askquestion("文件未保存", "要在保存文件之后打开文件吗")
                    if a_very_important_choice:
                        file1.write(textarea.get("1.0", "end"))
    def cover_the_textarea():
        with open(open_file_path, mode="r", encoding="utf-8") as file2:
            textarea.delete("1.0", "end")
            textarea.insert("1.0", file2.read())
    file_path = tkinter.filedialog.askopenfilename(title="開くファイルは。。。？")
    if file_path == "":
        tkinter.messagebox.showinfo("害tm带着那眼镜呢？文件那？", "我问你文件内，我文件呐？我文件啊啊啊啊啊！！！！！")
        return 0
    did_you_save_the_file()
    open_file_path = file_path
    cover_the_textarea()

def save_the_file():
    with open(open_file_path, mode="w", encoding="utf-8") as file1:
       file1.write(textarea.get("1.0", "end"))

rtwin = tk.Tk()

rtwin.title("Tedix v0.1.0")
rtwin.geometry("800x600")

mainmenu = tk.Menu(rtwin)

filemenu = tk.Menu(mainmenu, tearoff=False)
filemenu.add_command(label="新建")
filemenu.add_command(label="打开", command=open_file)
filemenu.add_command(label="保存", command=save_the_file)
filemenu.add_command(label="另存为", command=saveas_file)
filemenu.add_separator()
filemenu.add_command(label="退出", command=sys.exit)
helpmenu = tk.Menu(mainmenu, tearoff=False)
helpmenu.add_command(label="关于", command=win2_help)
helpmenu.add_command(label="输入注册码", command=sign_up_tedix)
mainmenu.add_cascade(label="文件", menu=filemenu)
mainmenu.add_cascade(label="帮助", menu=helpmenu)

textarea = tk.Text(rtwin)
textarea.place(relx=0, rely=0, relheight=1.0, relwidth=0.618)


subtextarea = tk.Text(rtwin)
subtextarea.place(relx=0.618, rely=0, relwidth=0.382, relheight=0.618)
infotextarea = tk.Text(rtwin)
infotextarea.place(relx=0.618, rely=0.618, relwidth=0.382, relheight=0.382)

rtwin.bind("<Control-S>", save_the_file)

rtwin.config(menu=mainmenu)
rtwin.mainloop()