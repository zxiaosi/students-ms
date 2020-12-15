# @Time : 2020/12/14 17:48 
# @Author : 小四先生
# @File : admin_modify.py
# @Version : 1.0
# @Description : 修改界面
import tkinter
import tkinter.messagebox

from db.HandleDB import HandleMysql
from view.base import BaseView


class ModifyAdmin(BaseView):
    def __init__(self):
        super().__init__()

    def modify_view(self):
        # 标题
        self.label_title = tkinter.Label(self.root, text='请输入要修改学生的学号: ', font=('黑体', 20))
        self.label_title.grid(row=0, columnspan=4, padx=140, pady=40)

        # 输入框
        self.ey_sno = tkinter.Entry(self.root, width=26)
        self.ey_sno.grid(row=1, column=1, sticky=tkinter.E)

        # 确定
        self.btn_sure = tkinter.Button(self.root, text='确定', width=8, command=self.sure)
        self.btn_sure.grid(row=1, column=2, sticky=tkinter.W)

        self.frame_label = tkinter.Frame(self.root)
        # 学号
        self.label_sno = tkinter.Label(self.frame_label, text='学 号 :', font=('宋体', 14))
        self.label_sno.grid(row=0, column=1, sticky=tkinter.W, pady=20)
        self.entry_sno = tkinter.Entry(self.frame_label)
        self.entry_sno.grid(row=1, column=1, sticky=tkinter.W)

        # 姓名
        self.label_sname = tkinter.Label(self.frame_label, text='姓 名 :', font=('宋体', 14))
        self.label_sname.grid(row=0, column=3, sticky=tkinter.W, pady=20)
        self.entry_sname = tkinter.Entry(self.frame_label)
        self.entry_sname.grid(row=1, column=3, sticky=tkinter.W)

        # 空白
        self.label_no = tkinter.Label(self.frame_label, width=16)
        self.label_no.grid(row=0, column=2)

        # 年龄
        self.label_sage = tkinter.Label(self.frame_label, text='年龄 :', font=('宋体', 14))
        self.label_sage.grid(row=2, column=1, sticky=tkinter.W, pady=20)
        self.entry_sage = tkinter.Entry(self.frame_label)
        self.entry_sage.grid(row=3, column=1, sticky=tkinter.W)

        # 班级
        self.label_sclass = tkinter.Label(self.frame_label, text='班 级 :', font=('宋体', 14))
        self.label_sclass.grid(row=2, column=3, sticky=tkinter.W, pady=20)
        self.entry_sclass = tkinter.Entry(self.frame_label)
        self.entry_sclass.grid(row=3, column=3, sticky=tkinter.W)

        self.frame_label.grid(row=2, columnspan=4)

        self.frame_btn = tkinter.Frame(self.root)
        self.btn_append = tkinter.Button(self.frame_btn, text='提交', width=20, height=2, command=self.submit)
        self.btn_append.grid(row=0, column=1, padx=40)
        self.btn_reset = tkinter.Button(self.frame_btn, text='重置', width=20, height=2, command=self.reset)
        self.btn_reset.grid(row=0, column=2, padx=40)
        self.frame_btn.grid(row=3, columnspan=4, pady=40)

        self.root.mainloop()  # 界面运行

    def sure(self):
        # 获取输入框内的值
        sno = self.ey_sno.get()
        print(sno)
        if sno == '':
            self.warning('学号不能为空！')
        else:
            self.select_no(sno)
            result = HandleMysql().select_student(sno)
            self.entry_sno.insert(0, f'{result[0]}')
            self.entry_sname.insert(0, f'{result[1]}')
            self.entry_sage.insert(0, f'{result[2]}')
            self.entry_sclass.insert(0, f'{result[3]}')

    def submit(self):
        osno = self.ey_sno.get()
        nsno = self.entry_sno.get()
        sname = self.entry_sname.get()
        sage = self.entry_sage.get()
        sclass = self.entry_sclass.get()

        list = [nsno, sname, sage, sclass]
        print(list)
        flag = self.none_value(list)
        if not flag:
            result = HandleMysql().select(nsno)
            if osno != nsno:
                if result == 1:
                    self.warning('学号已存在！')
                else:
                    # print(nsno, sname, sage, sclass, osno)
                    HandleMysql().update_student(nsno, sname, sage, sclass, osno)
                    self.success('修改成功！')
            else:
                # print(nsno, sname, sage, sclass, osno)
                HandleMysql().update_student(nsno, sname, sage, sclass, osno)
                self.success('修改成功！')


    # 重置
    def reset(self):
        # 获取输入框内的值
        len_no = len(self.ey_sno.get())
        len_sno = len(self.entry_sno.get())
        len_sname = len(self.entry_sname.get())
        len_sage = len(self.entry_sage.get())
        len_sclass = len(self.entry_sclass.get())

        self.ey_sno.delete(0, len_no)
        self.entry_sno.delete(0, len_sno)
        self.entry_sname.delete(0, len_sname)
        self.entry_sage.delete(0, len_sage)
        self.entry_sclass.delete(0, len_sclass)


if __name__ == '__main__':
    modify = ModifyAdmin()
    modify.modify_view()
