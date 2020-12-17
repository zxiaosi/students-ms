# @Time : 2020/12/14 17:20 
# @Author : 小四先生
# @File : v_admin.py
# @Version : 3.0
# @Description : 管理员界面
from view.base import BaseView
from view.admin.admin_append import AppendAdmin
from view.admin.admin_delete import DeleteAdmin
from view.admin.admin_modify import ModifyAdmin
from view.admin.admin_show import ShowAdmin
from view.admin.admin_showAll import ShowAllAdmin


class Admin(BaseView):
    def __init__(self):
        super().__init__()

    # 管理员界面
    def admin_view(self):
        """ 管理员界面 """

        # 标题
        self.label_title(text='欢迎使用学生信息管理系统', columnspan=1, padx=105, pady=20)

        # 添加按钮
        self.button(name='append', text='添    加', height=2, command=self.append_view, row=1)

        # 查询按钮
        self.button(name='select', text='查    询', height=2, command=self.show_view, row=2)

        # 删除按钮
        self.button(name='delete', text='删    除', height=2, command=self.delete_view, row=3)

        # 查询所有按钮
        self.button(name='delete', text='查询所有', height=2, command=self.showAll_view, row=4)

        # 修改按钮
        self.button(name='modify', text='修    改', height=2, command=self.modify_view, row=5)

        # 退出系统按钮
        self.button(name='quit', text='退出系统', height=2, command=self.root.destroy, row=6)

        self.root.mainloop()  # 界面运行

    # 实例化添加界面
    def append_view(self):
        append = AppendAdmin()
        append.append_view()

    # 实例化查询界面
    def show_view(self):
        show = ShowAdmin()
        show.show_view()

    # 实例化删除界面
    def delete_view(self):
        delete = DeleteAdmin()
        delete.delete_view()

    # 实例化查询所有界面
    def showAll_view(self):
        showall = ShowAllAdmin()
        showall.showAll_view()

    # 实例化修改界面
    def modify_view(self):
        modify = ModifyAdmin()
        modify.modify_view()


# if __name__ == '__main__':
#     admin = Admin()
#     admin.admin_view()
