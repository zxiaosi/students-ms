# @Time : 2020/12/14 17:44 
# @Author : 小四先生
# @File : admin_show.py
# @Version : 3.0
# @Description : 查询界面
import tkinter
import tkinter.messagebox

from view.base import BaseView
from db.HandleDB import HandleMysql


class ShowAdmin(BaseView):
    """ 查询学生信息的类 """

    def __init__(self):
        super().__init__()

    # 查询界面
    def show_view(self):
        """ 查询界面 """
        # 标题
        self.label_title(text='请输入要查询学生的学号: ', padx=110, pady=40)

        # 学号
        self.entry_sno = self.entry(name='sno', row=1, column=1, width=36)

        # 查找和重置按钮
        self.frame_button(name1='select', name2='reset', text1='查找', text2='重置',
                          btn1_command=self.select, btn2_command=self.reset,
                          row=2, pady=20)

        # 输出框
        self.listbox = tkinter.Listbox(self.root, width=34, selectmode=tkinter.EXTENDED)
        self.listbox.grid(row=3, columnspan=2)

        # 清空按钮
        self.button(name='empty', text='清    空', width=30, height=2,
                    command=self.listbox_empty, row=4, column=1, sticky=tkinter.W, pady=20)

        self.root.mainloop()  # 界面运行

    # 向listbox中添加文字
    def list_box(self, n):
        """
        :param n: 数字
        :type n: int
        :return: 返回数字对应的字符串
        """

        if n == 0:
            return '学 号'
        elif n == 1:
            return '姓 名'
        elif n == 2:
            return '年 龄'
        elif n == 3:
            return '班 级'

    # 添加按钮
    def select(self):
        """ 检测、查询学生信息 """

        # 获取输入框内的值
        sno = self.entry_sno.get()
        if sno == '':
            self.warning('学号不能为空！')
        else:
            # 获取数据库中管理员账户与密码
            self.select_no(sno)
            self.listbox.insert(0, '-' * 20)
            result = HandleMysql().select_student(sno)
            for n in range(len(result)):
                self.listbox.insert(n, f'{self.list_box(n)}: {result[n]}')
                self.listbox.select_set(n)

    # 重置按钮
    def reset(self):
        """ 清空输入框内的数据 """

        # 获取输入框内的值
        sno = self.entry_sno.get()

        len_sno = len(sno)
        self.entry_sno.delete(0, len_sno)

    # 清空
    def listbox_empty(self):
        """ 清空列表框内的数据 """

        self.listbox.delete(0, tkinter.END)


# if __name__ == '__main__':
#     show = ShowAdmin()
#     show.show_view()
