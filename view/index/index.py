# @Time : 2020/12/14 11:00 
# @Author : 小四先生
# @File : index.py
# @Version : 1.0
# @Description : 用户登录界面

# 导入tkinter 包
import tkinter
import tkinter.messagebox

from db.HandleDB import HandleMysql
from view.base import BaseView
from view.admin.v_admin import Admin


class Index(BaseView):
    def __init__(self):
        super().__init__()

    # 主界面
    def index_view(self):
        # 标题
        self.label_title = tkinter.Label(self.root, text='欢迎使用学生信息管理系统', font=('黑体', 24))
        self.label_title.grid(row=0, columnspan=2, padx=105, pady=60)

        # 账户
        self.label_user = tkinter.Label(self.root, text='账  号 :', font=('宋体', 14))
        self.label_user.grid(row=1, sticky=tkinter.E, pady=20)
        self.entry_user = tkinter.Entry(self.root)
        self.entry_user.grid(row=1, column=1, sticky=tkinter.W)

        # 密码
        self.label_pwd = tkinter.Label(self.root, text='密  码 :', font=('宋体', 14))
        self.label_pwd.grid(row=2, sticky=tkinter.E, pady=20)
        self.entry_pwd = tkinter.Entry(self.root)
        self.entry_pwd['show'] = '*'  # 隐藏显示
        self.entry_pwd.grid(row=2, column=1, sticky=tkinter.W)

        # 登录和退出按钮
        self.frame_btn = tkinter.Frame(self.root)
        self.btn_login = tkinter.Button(self.frame_btn, text='登录', width=10, command=self.login)
        self.btn_login.grid(row=0, column=0, padx=40)
        self.btn_regist = tkinter.Button(self.frame_btn, text='退出', width=10, command=self.root.destroy)
        self.btn_regist.grid(row=0, column=1, padx=40)
        self.frame_btn.grid(row=3, columnspan=2, pady=40)

        self.root.mainloop()  # 界面运行

    # 登录
    def login(self):
        # 获取数据库中管理员账户与密码
        handle = HandleMysql()
        user, pwd = handle.select_user()

        # 获取输入框内的值
        username = self.entry_user.get()
        passwd = self.entry_pwd.get()
        len_pwd = len(passwd)
        if username == '' or passwd == '':
            self.warning('账号或密码不能为空！')
        else:
            if username == user and passwd == pwd:
                # self.success('登录成功！')
                # 销毁原窗口
                self.root.destroy()
                # 进入后台管理
                Admin().admin_view()
            else:
                self.fail('账号或密码错误！')

        self.entry_pwd.delete(0, len_pwd)


if __name__ == '__main__':
    index = Index()
    index.index_view()
