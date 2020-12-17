# @Time : 2020/12/16 18:03 
# @Author : 小四先生
# @File : connect.py
# @Version : 3.0
# @Description : 连接数据库
import tkinter.messagebox

from db import InitializeDB
from db.LogDB import deal_with
from lib.ConnectDB import ConnMysql
from view.index.index import Index


def try_except(func):
    """ 异常装饰器 """

    def decorator():
        try:
            tk = tkinter.Tk()
            tk.after(3000, lambda: tk.destroy())  # 3秒后销毁小部件
            tk.withdraw()
            func()
            if tkinter.messagebox.OK:
                tk.destroy()
                tk.mainloop()
        except Exception:
            print(Exception)

    return decorator


# 连接数据时的弹窗
@try_except
def conn():
    tkinter.messagebox.showinfo('提示', '正在连接数据库...')


# 初始化数据时的弹窗
@try_except
def init():
    tkinter.messagebox.showinfo('提示', '正在初始化数据...')


# 连接失败时的弹窗
@try_except
def fail():
    tkinter.messagebox.showerror('错误', '连接数据库失败！！！')


# 初始化数据库
def InitDB(flag=True):
    """ 初始化数据库 """

    if flag:
        init = InitializeDB.InitMysql()
        # init.create_database()
        init.create_table()
        init.insert_data()


# 处理函数
def deal():
    conn()
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


# if __name__ == '__main__':
#     deal()
