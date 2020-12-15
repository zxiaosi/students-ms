# @Time : 2020/12/14 17:44 
# @Author : 小四先生
# @File : admin_show.py
# @Version : 1.0
# @Description : 查询界面
import tkinter
import tkinter.messagebox

from view.base import BaseView
from db.HandleDB import HandleMysql


class ShowAdmin(BaseView):
    def __init__(self):
        super().__init__()

    def show_view(self):
        # 标题
        self.label_title = tkinter.Label(self.root, text='请输入要查询学生的学号: ', font=('黑体', 20))
        self.label_title.grid(row=0, columnspan=2, padx=140, pady=40)

        # 学号
        self.entry_sno = tkinter.Entry(self.root, width=36)
        self.entry_sno.grid(row=1, column=1, sticky=tkinter.W)

        # 查找和重置按钮
        self.frame_btn = tkinter.Frame(self.root)
        self.btn_append = tkinter.Button(self.frame_btn, text='查找', width=10, command=self.select)
        self.btn_append.grid(row=0, column=0, padx=40)
        self.btn_reset = tkinter.Button(self.frame_btn, text='重置', width=10, command=self.reset)
        self.btn_reset.grid(row=0, column=1, padx=40)
        self.frame_btn.grid(row=2, columnspan=2, pady=20)

        # 输出框
        self.listbox = tkinter.Listbox(self.root, width=34, selectmode=tkinter.EXTENDED)
        self.listbox.grid(row=3, columnspan=2)

        # 清空按钮
        self.button_empty = tkinter.Button(self.root, text='清    空', width=30, height=2,
                                           font=('黑体', 12), command=self.empty)
        self.button_empty.grid(row=4, column=1, pady=20, sticky=tkinter.W)

        self.root.mainloop()  # 界面运行

    # 向listbox中添加文字
    def list_box(self, n):
        if n == 0:
            return '学 号'
        elif n == 1:
            return '姓 名'
        elif n == 2:
            return '年 龄'
        elif n == 3:
            return '班 级'

    # 添加数据
    def select(self):
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

    # 重置
    def reset(self):
        # 获取输入框内的值
        sno = self.entry_sno.get()

        len_sno = len(sno)
        self.entry_sno.delete(0, len_sno)

    def empty(self):
        self.listbox.delete(0, tkinter.END)


if __name__ == '__main__':
    show = ShowAdmin()
    show.show_view()
