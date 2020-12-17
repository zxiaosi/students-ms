# @Time : 2020/12/14 17:47 
# @Author : 小四先生
# @File : admin_showAll.py
# @Version : 3.0
# @Description : 显示所有学生信息界面
from view.base import BaseView


class ShowAllAdmin(BaseView):
    """ 显示所有学生信息的类 """

    def __init__(self):
        super().__init__()

    # 显示数据界面
    def showAll_view(self):
        """ 显示数据界面 """
        # 标题
        self.label_title(text='学 生 信 息 : ', padx=200, pady=40)

        # 列表框
        self.treeview(row=1, columnspan=2)

        # 刷新和返回按钮
        self.frame_button(name1='refresh', name2='quit', text1='刷新', text2='返回',
                          width=20, height=2, btn1_command=self.show, btn2_command=self.root.destroy,
                          row=2, pady=40)

        self.root.mainloop()  # 界面运行


# if __name__ == '__main__':
#     show = ShowAllAdmin()
#     show.showAll_view()
