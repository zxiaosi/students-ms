# @Time : 2020/12/14 17:20 
# @Author : 小四先生
# @File : v_admin.py
# @Version : 1.0
# @Description : 管理员界面
# 导入tkinter 包
import tkinter
import tkinter.messagebox


from view.base import BaseView
from view.admin.admin_append import AppendAdmin
from view.admin.admin_delete import DeleteAdmin
from view.admin.admin_modify import ModifyAdmin
from view.admin.admin_show import ShowAdmin
from view.admin.admin_showAll import ShowAllAdmin


class Admin(BaseView):
    def __init__(self):
        super().__init__()

    def admin_view(self):
        # 标题
        self.label_title = tkinter.Label(self.root, text='欢迎使用学生信息管理系统', font=('黑体', 24))
        self.label_title.grid(row=0, padx=105, pady=20)

        # 添加按钮
        self.button_add = tkinter.Button(self.root, text='添    加', width=24, height=2,
                                         font=('黑体', 12), command=self.append_view)
        self.button_add.grid(row=1, pady=10)

        # 查询按钮
        self.button_add = tkinter.Button(self.root, text='查    询', width=24, height=2,
                                         font=('黑体', 12), command=self.show_view)
        self.button_add.grid(row=2, pady=10)

        # 删除按钮
        self.button_add = tkinter.Button(self.root, text='删    除', width=24, height=2,
                                         font=('黑体', 12), command=self.delete_view)
        self.button_add.grid(row=3, pady=10)

        # 查询所有按钮
        self.button_add = tkinter.Button(self.root, text='查询所有', width=24, height=2,
                                         font=('黑体', 12), command=self.showAll_view)
        self.button_add.grid(row=4, pady=10)

        # 修改按钮
        self.button_add = tkinter.Button(self.root, text='修    改', width=24, height=2,
                                         font=('黑体', 12), command=self.modify_view)
        self.button_add.grid(row=5, pady=10)

        # 退出系统按钮
        self.button_add = tkinter.Button(self.root, text='退出系统', width=24, height=2,
                                         font=('黑体', 12), command=self.root.destroy)
        self.button_add.grid(row=6, pady=10)

        self.root.mainloop()  # 界面运行

    def append_view(self):
        append = AppendAdmin()
        append.append_view()

    def show_view(self):
        show = ShowAdmin()
        show.show_view()

    def delete_view(self):
        delete = DeleteAdmin()
        delete.delete_view()

    def showAll_view(self):
        showall = ShowAllAdmin()
        showall.showAll_view()

    def modify_view(self):
        modify = ModifyAdmin()
        modify.modify_view()


if __name__ == '__main__':
    admin = Admin()
    admin.admin_view()
