# @Time : 2020/12/14 17:48 
# @Author : 小四先生
# @File : admin_modify.py
# @Version : 3.0
# @Description : 修改界面
import tkinter
import tkinter.messagebox

from db.HandleDB import HandleMysql
from view.base import BaseView


class ModifyAdmin(BaseView):
    """ 修改学生信息的类 """

    def __init__(self):
        super().__init__()

    # 修改界面
    def modify_view(self):
        """ 修改界面 """
        # 标题
        self.label_title(text='请输入要修改学生的学号: ', columnspan=4, padx=120, pady=40)

        # 输入框
        self.ey_sno = self.entry(name='ey_sno', row=1, column=1, width=26, sticky=tkinter.E)

        # 确定
        self.button(name='sure', text='确定', width=8, command=self.sure,
                    row=1, column=2, sticky=tkinter.W, pady=5)

        # 学号
        self.label(name='sno', text='学 号 :', row=2, column=1, sticky=tkinter.W, padx=60, pady=20)
        self.entry_sno = self.entry(name='sno', row=3, column=1, padx=60)

        # 姓名
        self.label(name='sname', text='姓 名:', row=2, column=2, sticky=tkinter.W, pady=20)
        self.entry_sname = self.entry(name='sname', row=3, column=2)

        # 年龄
        self.label(name='sage', text='年 龄 :', row=4, column=1, sticky=tkinter.W, padx=60, pady=20)
        self.entry_sage = self.entry(name='sage', row=5, column=1, padx=60)

        # 班级
        self.label(name='sclass', text='姓 名:', row=4, column=2, sticky=tkinter.W, pady=20)
        self.entry_sclass = self.entry(name='sclass', row=5, column=2)

        # 提交和重置按钮
        self.frame_button(name1='submit', name2='reset', text1='提交', text2='重置',
                          width=20, height=2, btn1_command=self.submit, btn2_command=self.reset,
                          row=10, column=1, columnspan=4, pady=40)

        self.root.mainloop()  # 界面运行

    # 确定按钮
    def sure(self):
        """ 查询学生信息 """

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

    # 提交按钮
    def submit(self):
        """ 检测、修改学生信息 """

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

    # 重置按钮
    def reset(self):
        """ 清空输入框内的数据 """

        self.ey_sno.delete(0, len(self.ey_sno.get()))
        self.entry_sno.delete(0, len(self.entry_sno.get()))
        self.entry_sname.delete(0, len(self.entry_sname.get()))
        self.entry_sage.delete(0, len(self.entry_sage.get()))
        self.entry_sclass.delete(0, len(self.entry_sclass.get()))


# if __name__ == '__main__':
#     modify = ModifyAdmin()
#     modify.modify_view()
