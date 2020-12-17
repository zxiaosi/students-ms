# @Time : 2020/12/14 11:00 
# @Author : 小四先生
# @File : index.py
# @Version : 3.0
# @Description : 用户登录界面

from db.HandleDB import HandleMysql
from view.base import BaseView
from view.admin.v_admin import Admin


class Index(BaseView):
    """ 主界面的类 """

    def __init__(self):
        super().__init__()

    # 主界面
    def index_view(self):
        """ 主界面 """
        # 标题
        self.label_title(text='欢迎使用学生信息管理系统', padx=120, pady=60)

        # 账户
        self.label(name='user', text='账  号 :', row=1, pady=20)
        self.entry_user = self.entry(name='user', row=1, column=1)

        # 密码
        self.label(name='pwd', text='密  码 :', row=2, pady=20)
        self.entry_pwd = self.entry(name='pwd', row=2, column=1)

        # 登录和退出按钮
        self.frame_button(name1='login', name2='regist', text1='登录', text2='退出',
                          btn1_command=self.login, btn2_command=self.root.destroy, )

        self.root.mainloop()  # 界面运行

    # 登录按钮
    def login(self):
        """ 检测、对比管理员信息 """

        # 获取数据库中管理员账户与密码
        handle = HandleMysql()
        result = handle.select_user()

        # 获取输入框内的值
        username = self.entry_user.get()
        passwd = self.entry_pwd.get()
        len_pwd = len(passwd)

        if username == '' or passwd == '':
            self.warning('账号或密码不能为空！')
        else:
            if username == result[0] and passwd == result[1]:
                # self.success('登录成功！')
                # 销毁原窗口
                self.root.destroy()
                # 进入后台管理
                Admin().admin_view()
            else:
                self.fail('账号或密码错误！')

        self.entry_pwd.delete(0, len_pwd)


# if __name__ == '__main__':
#     index = Index()
#     index.index_view()
