# @Time : 2020/12/14 16:38 
# @Author : 小四先生
# @File : base.py
# @Version : 1.0
# @Description : 定义模板父类
import tkinter
import tkinter.messagebox

from db.HandleDB import HandleMysql


class BaseView(object):
    def __init__(self):
        # 创建 tkinter 应用程序主窗口
        self.root = tkinter.Tk()
        # 窗口大小
        self.root.geometry('600x500+300+150')
        # 固定窗口
        self.root.resizable(width=False, height=False)
        # 窗口标题
        self.root.title('学生信息管理系统')

    def select_no(self, sno):
        # 查询学号是否重复
        result = HandleMysql().select(sno)
        if result == 0:
            self.warning('学号不存在！')

    def none_value(self, list):
        flag = True
        if list[0] == '':
            self.warning('学号不能为空！')
        elif list[1] == '':
            self.warning('名字不能为空！')
        elif list[2] == '':
            self.warning('年龄不能为空！')
        elif list[3] == '':
            self.warning('班级不能为空！')
        else:
            flag = False
        return flag

    # 提示弹窗
    def success(self, msg='成功！'):
        # 弹出对话框
        tkinter.messagebox.showinfo('提示', msg, parent=self.root)

    # 错误弹窗
    def fail(self, msg='错误！'):
        # 弹出对话框
        tkinter.messagebox.showerror('错误', msg, parent=self.root)

    # 警告弹窗
    def warning(self, msg='警告！'):
        # 弹出对话框
        tkinter.messagebox.showwarning('警告', msg, parent=self.root)


if __name__ == '__main__':
    base = BaseView()
    # base.success()
    # base.fail()
    # base.warning()

    base.select_no(1006)
