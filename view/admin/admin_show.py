# @Time : 2020/12/14 17:44 
# @Author : 小四先生
# @File : admin_show.py
# @Version : 1.0
# @Description : 查询界面
import tkinter
import tkinter.messagebox

from view.base import BaseView


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

        # 登录和注册按钮
        self.frame_btn = tkinter.Frame(self.root)
        self.btn_append = tkinter.Button(self.frame_btn, text='查找', width=10)
        self.btn_append.grid(row=0, column=0, padx=40)
        self.btn_reset = tkinter.Button(self.frame_btn, text='重置', width=10)
        self.btn_reset.grid(row=0, column=1, padx=40)
        self.frame_btn.grid(row=2, columnspan=2, pady=20)

        # 输出框
        self.listbox = tkinter.Listbox(self.root, width=34)
        self.listbox.grid(row=3, columnspan=2)

        # 清空按钮
        self.button_add = tkinter.Button(self.root, text='清    空', width=30, height=2,
                                         font=('黑体', 12))
        self.button_add.grid(row=4, column=1, pady=20, sticky=tkinter.W)

        self.root.mainloop()  # 界面运行


if __name__ == '__main__':
    show = ShowAdmin()
    show.show_view()