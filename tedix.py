import tkinter as tk
import _thread
import sys
import webbrowser
import random

def open_buy_web(event):
    webbrowser.open("https://tedix.rth1.one/buy", new=0)

def win2_help():
    win2 = tk.Toplevel()
    win2.geometry("400x300")
    win2.resizable(False, False)
    # tk.Label(win2, image=tk.PhotoImage(file="tedix.gif")).pack()
    tk.Label(win2, text="Tedix").pack()
    tk.Label(win2, text="一个简单的文本编辑器").pack()
    tk.Label(win2, text="作者: Joulier429").pack()
    tk.Button(win2, text="确定", command=win2.destroy).place(relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1)

def sign_up_tedix():
    global the_key
    win3 = tk.Toplevel()
    win3.geometry("400x300")
    win3.title("输入注册码")
    win3.resizable(False, False)
    tk.Label(win3, text="请在请在下面输入您的密钥，").pack()
    url = tk.Label(win3, text="您可以在 https://tedix.rth1.one/buy 购买", fg="#1D6A96")
    url.pack()
    url.bind("<Button-1>", open_buy_web)
    tk.Button(win3, text="确定", command=nothing_like_that).place(relx=0.3, rely=0.87, relheight=0.1, relwidth=0.4)
    license_text_area = tk.Text(win3)
    license_text_area.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.7)
    def nothing_like_that():
        win4 = tk.Toplevel()
        a = the_key
        if a:
            b = "没有像那样东西😡"
        elif not a:
            b = "这是我们信任的问题😡"
        win4.title("没有像那样东西😡")
        win4.geometry("300x100")
        tk.Label(win4, text="没有像那样东西😡").pack()
        tk.Button(win4, text="确定", command=win4.destroy).pack()
        win4.resizable(False, False)
        


def open_a_file(): # 打开文件
    pass

rtwin = tk.Tk()

rtwin.title("Tedix")
rtwin.geometry("800x600")

mainmenu = tk.Menu(rtwin)

filemenu = tk.Menu(mainmenu, tearoff=False)
filemenu.add_command(label="新建")
filemenu.add_command(label="保存")
filemenu.add_command(label="另存为")
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

rtwin.config(menu=mainmenu)
rtwin.mainloop()