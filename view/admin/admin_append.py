# @Time : 2020/12/14 17:40 
# @Author : 小四先生
# @File : admin_append.py
# @Version : 3.0
# @Description : 添加页面
from view.base import BaseView
from db.HandleDB import HandleMysql


class AppendAdmin(BaseView):
    """ 添加学生信息的类 """

    def __init__(self):
        super().__init__()

    # 添加页面
    def append_view(self):
        # 标题
        self.label_title(text='添 加 学 生', padx=220, pady=30)

        # 学号
        self.label(name='sno', text='学 号 :', row=1, pady=20)
        self.entry_sno = self.entry('sno', row=1, column=1)

        # 学生名
        self.label(name='sname', text='姓 名 :', row=2, pady=20)
        self.entry_sname = self.entry('sname', row=2, column=1)

        # 年龄
        self.label(name='sage', text='年 龄 :', row=3, pady=20)
        self.entry_sage = self.entry('sage', row=3, column=1)

        # 班级
        self.label(name='sclass', text='班 级 :', row=4, pady=20)
        self.entry_sclass = self.entry('sclass', row=4, column=1)

        # 添加和重置按钮
        self.frame_button(name1='append', name2='reset', text1='添加', text2='重置',
                          btn1_command=self.append, btn2_command=self.reset,
                          row=5, pady=40)

        self.root.mainloop()  # 界面运行

    # 获取数据
    def accept_data(self):
        """
        :return: 获取输入内的数据,并以列表的形式返回
        """

        # 获取输入框内的值
        data = [self.entry_sno.get(),
                self.entry_sname.get(),
                self.entry_sage.get(),
                self.entry_sclass.get()]

        return data

    # 添加按钮
    def append(self):
        """ 检测、添加学生信息 """

        data = self.accept_data()
        flag = self.none_value(data)
        if not flag:
            # 调用父类的方法
            self.select_no(data[0], False)

            self.success('添加成功！')
            HandleMysql().add_student(*data)

    # 重置按钮
    def reset(self):
        """ 清空输入框内的数据 """

        data = self.accept_data()

        self.entry_sno.delete(0, len(data[0]))
        self.entry_sname.delete(0, len(data[1]))
        self.entry_sage.delete(0, len(data[2]))
        self.entry_sclass.delete(0, len(data[3]))


# if __name__ == '__main__':
#     app = AppendAdmin()
#     app.append_view()
