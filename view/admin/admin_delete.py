# @Time : 2020/12/14 17:46 
# @Author : 小四先生
# @File : admin_delete.py
# @Version : 1.0
# @Description : 删除界面
import tkinter
import tkinter.messagebox
from tkinter import ttk

from view.base import BaseView
from db.HandleDB import HandleMysql


class DeleteAdmin(BaseView):
    def __init__(self):
        super().__init__()

    def delete_view(self):
        # 标题
        self.label_title = tkinter.Label(self.root, text='请输入要删除学生的学号: ', font=('黑体', 20))
        self.label_title.grid(row=0, columnspan=2, padx=140, pady=20)

        # 学号
        self.entry_sno = tkinter.Entry(self.root, width=34)
        self.entry_sno.grid(row=1, column=1, sticky=tkinter.W)

        # 删除和重置按钮
        self.frame_btn = tkinter.Frame(self.root)
        self.btn_delete = tkinter.Button(self.frame_btn, text='删除', width=10, command=self.delete)
        self.btn_delete.grid(row=0, column=0, padx=40)
        self.btn_reset = tkinter.Button(self.frame_btn, text='重置', width=10, command=self.reset)
        self.btn_reset.grid(row=0, column=1, padx=40)
        self.frame_btn.grid(row=2, columnspan=2, pady=20)

        # 列表框
        self.dataTreeview = ttk.Treeview(self.root, show='headings', column=('sid', 'name', 'phone', 'address'))
        self.dataTreeview.column('sid', width=120, anchor="center")
        self.dataTreeview.column('name', width=120, anchor="center")
        self.dataTreeview.column('phone', width=120, anchor="center")
        self.dataTreeview.column('address', width=120, anchor="center")

        self.dataTreeview.heading('sid', text='学号')
        self.dataTreeview.heading('name', text='名字')
        self.dataTreeview.heading('phone', text='年龄')
        self.dataTreeview.heading('address', text='班级')

        self.dataTreeview.grid(row=3, columnspan=2)

        # 刷新和返回按钮
        self.frame_btn = tkinter.Frame(self.root)
        self.btn_append = tkinter.Button(self.frame_btn, text='刷新', width=20, height=2, command=self.show)
        self.btn_append.grid(row=0, column=0, padx=40)
        self.btn_reset = tkinter.Button(self.frame_btn, text='返回', width=20, height=2, command=self.root.destroy)
        self.btn_reset.grid(row=0, column=1, padx=40)
        self.frame_btn.grid(row=4, columnspan=2, pady=20)

        self.root.mainloop()  # 界面运行

    # 删除
    def delete(self):
        # 获取输入框内的值
        sno = self.entry_sno.get()
        if sno == '':
            self.warning('学号不能为空！')
        else:
            result = HandleMysql().select(sno)
            if result == 1:
                HandleMysql().delete_student(sno)
                self.success('删除成功！')
            else:
                self.warning('学号不存在')

    # 重置
    def reset(self):
        # 获取输入框内的值
        sno = self.entry_sno.get()

        len_sno = len(sno)
        self.entry_sno.delete(0, len_sno)

    def show(self):
        self.empty(self.dataTreeview)
        list = HandleMysql().student_list()
        for item in list:
            self.dataTreeview.insert("", 1, text="line1", values=item)

    def empty(self, tree):
        x = tree.get_children()
        for item in x:
            tree.delete(item)


if __name__ == '__main__':
    delete = DeleteAdmin()
    delete.delete_view()
