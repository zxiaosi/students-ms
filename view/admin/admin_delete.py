# @Time : 2020/12/14 17:46 
# @Author : 小四先生
# @File : admin_delete.py
# @Version : 3.0
# @Description : 删除界面
from view.base import BaseView
from db.HandleDB import HandleMysql


class DeleteAdmin(BaseView):
    """ 删除学生信息的类 """

    def __init__(self):
        super().__init__()

    # 删除界面
    def delete_view(self):
        """ 删除界面 """

        # 标题
        self.label_title(text='请输入要删除学生的学号: ', padx=115, pady=20)

        # 学号
        self.entry_sno = self.entry(name='sno', width=34, row=1, column=1)

        # 删除和重置按钮
        self.frame_button(name1='delete', name2='reset', text1='删除', text2='重置',
                          btn1_command=self.delete, btn2_command=self.reset,
                          row=2, pady=20)

        # 列表框
        self.treeview(row=3, columnspan=2)

        # 刷新和返回按钮
        self.frame_button(name1='refresh', name2='quit', text1='刷新', text2='返回',
                          width=20, height=2, btn1_command=self.show, btn2_command=self.root.destroy,
                          row=4, pady=20)

        self.root.mainloop()  # 界面运行

    # 删除按钮
    def delete(self):
        """ 检测、删除学生信息 """

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

    # 重置按钮
    def reset(self):
        """ 清空输入框内的数据 """

        # 获取输入框内的值
        sno = self.entry_sno.get()

        len_sno = len(sno)
        self.entry_sno.delete(0, len_sno)


# if __name__ == '__main__':
#     delete = DeleteAdmin()
#     delete.delete_view()
