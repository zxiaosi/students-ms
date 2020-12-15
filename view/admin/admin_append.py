# @Time : 2020/12/14 17:40 
# @Author : 小四先生
# @File : admin_append.py
# @Version : 1.0
# @Description : 添加页面

import tkinter
import tkinter.messagebox

from view.base import BaseView
from db.HandleDB import HandleMysql


class AppendAdmin(BaseView):
    def __init__(self):
        super().__init__()

    # 添加页面
    def append_view(self):
        # 标题
        self.label_title = tkinter.Label(self.root, text='添 加 学 生', font=('黑体', 24))
        self.label_title.grid(row=0, columnspan=2, padx=210, pady=20)

        # 学号
        self.label_sno = tkinter.Label(self.root, text='学 号 :', font=('宋体', 14))
        self.label_sno.grid(row=1, sticky=tkinter.E, pady=20)
        self.entry_sno = tkinter.Entry(self.root)
        self.entry_sno.grid(row=1, column=1, sticky=tkinter.W)

        # 学生名
        self.label_sname = tkinter.Label(self.root, text='学生名 :', font=('宋体', 14))
        self.label_sname.grid(row=2, sticky=tkinter.E, pady=20)
        self.entry_sname = tkinter.Entry(self.root)
        self.entry_sname.grid(row=2, column=1, sticky=tkinter.W)

        # 年龄
        self.label_sage = tkinter.Label(self.root, text='年 龄 :', font=('宋体', 14))
        self.label_sage.grid(row=3, sticky=tkinter.E, pady=20)
        self.entry_sage = tkinter.Entry(self.root)
        self.entry_sage.grid(row=3, column=1, sticky=tkinter.W)

        # 班级
        self.label_sclass = tkinter.Label(self.root, text='班 级 :', font=('宋体', 14))
        self.label_sclass.grid(row=4, sticky=tkinter.E, pady=20)
        self.entry_sclass = tkinter.Entry(self.root)
        self.entry_sclass.grid(row=4, column=1, sticky=tkinter.W)

        # 登录和注册按钮
        self.frame_btn = tkinter.Frame(self.root)
        self.btn_append = tkinter.Button(self.frame_btn, text='添加', width=10, command=self.append)
        self.btn_append.grid(row=0, column=0, padx=40)
        self.btn_reset = tkinter.Button(self.frame_btn, text='重置', width=10, command=self.reset)
        self.btn_reset.grid(row=0, column=1, padx=40)
        self.frame_btn.grid(row=5, columnspan=2, pady=40)

        self.root.mainloop()  # 界面运行

    # 添加数据
    def data(self):
        # 获取输入框内的值
        list = []
        sno = self.entry_sno.get()
        sname = self.entry_sname.get()
        sage = self.entry_sage.get()
        sclass = self.entry_sclass.get()
        list.append(sno)
        list.append(sname)
        list.append(sage)
        list.append(sclass)
        return list

    # 添加
    def append(self):
        list = self.data()
        flag = self.none_value(list)
        if not flag:
            # 调用父类的方法
            self.select_no(list[0])

            self.success('添加成功！')
            HandleMysql().add_student(*list)

    # 重置
    def reset(self):
        list = self.data()

        len_sno = len(list[0])
        len_sname = len(list[1])
        len_sage = len(list[2])
        len_sclass = len(list[3])

        self.entry_sno.delete(0, len_sno)
        self.entry_sname.delete(0, len_sname)
        self.entry_sage.delete(0, len_sage)
        self.entry_sclass.delete(0, len_sclass)


if __name__ == '__main__':
    app = AppendAdmin()
    app.append_view()
