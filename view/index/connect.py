# @Time : 2020/12/16 18:03 
# @Author : 小四先生
# @File : connect.py
# @Version : 1.0
# @Description : 连接数据库
import tkinter.messagebox

from db.LogDB import exist, InitDB, deal_with
from lib.ConnectDB import ConnMysql
from view.index.index import Index


def connect():
    try:
        tk = tkinter.Tk()
        tk.after(3000, lambda: tk.destroy())  # 3秒后销毁小部件
        tk.withdraw()
        tkinter.messagebox.showinfo('提示', '正在连接数据库...')
        if tkinter.messagebox.OK:
            tk.destroy()
            tk.mainloop()
            confirmation = '正在连接数据库...'
            print(confirmation)
    except Exception:
        confirmation = '正在连接数据库...'
        print(confirmation)


def init():
    try:
        tk = tkinter.Tk()
        tk.after(3000, lambda: tk.destroy())  # 3秒后销毁小部件
        tk.withdraw()
        tkinter.messagebox.showinfo('提示', '正在初始化数据...')
        if tkinter.messagebox.OK:
            tk.destroy()
            tk.mainloop()
            confirmation = '正在初始化数据...'
            print(confirmation)
    except Exception:
        confirmation = '正在初始化数据...'
        print(confirmation)


def fail():
    try:
        tk = tkinter.Tk()
        tk.after(3000, lambda: tk.destroy())  # 3秒后销毁小部件
        tk.withdraw()
        tkinter.messagebox.showerror('错误', '连接数据库失败！！！')
        if tkinter.messagebox.OK:
            tk.destroy()
            tk.mainloop()
            confirmation = '连接数据库失败！！！'
            print(confirmation)
    except Exception:
        confirmation = '连接数据库失败！！！'
        print(confirmation)


def deal():
    connect()
    reslut = ConnMysql().conn_mysql()
    if reslut:
        flag = deal_with()
        if flag:
            init()
            InitDB()
            Index().index_view()
        else:
            Index().index_view()
    else:
        fail()


if __name__ == '__main__':
    deal()
