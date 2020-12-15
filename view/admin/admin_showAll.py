# @Time : 2020/12/14 17:47 
# @Author : 小四先生
# @File : admin_showAll.py
# @Version : 1.0
# @Description : 查询所有界面
import tkinter
import tkinter.messagebox
from tkinter import ttk

from view.base import BaseView
from db.HandleDB import HandleMysql



class ShowAllAdmin(BaseView):
    def __init__(self):
        super().__init__()

    def showAll_view(self):
        # 标题
        self.label_title = tkinter.Label(self.root, text='学 生 信 息 : ', font=('黑体', 20))
        self.label_title.grid(row=0, columnspan=2, padx=210, pady=40)

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

        self.dataTreeview.grid(row=1, columnspan=2)

        # 刷新和返回按钮
        self.frame_btn = tkinter.Frame(self.root)
        self.btn_append = tkinter.Button(self.frame_btn, text='刷新', width=20, height=2, command=self.show)
        self.btn_append.grid(row=0, column=0, padx=40)
        self.btn_reset = tkinter.Button(self.frame_btn, text='返回', width=20, height=2, command=self.root.destroy)
        self.btn_reset.grid(row=0, column=1, padx=40)
        self.frame_btn.grid(row=2, columnspan=2, pady=40)

        self.root.mainloop()  # 界面运行

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
    show = ShowAllAdmin()
    show.showAll_view()
