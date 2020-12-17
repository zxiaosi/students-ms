# @Time : 2020/12/14 16:38 
# @Author : 小四先生
# @File : base.py
# @Version : 3.0
# @Description : 定义模板父类
import tkinter
import tkinter.messagebox
from tkinter import ttk

from db.HandleDB import HandleMysql


class BaseView(object):
    """ view的父类 """

    def __init__(self):
        # 创建 tkinter 应用程序主窗口
        self.root = tkinter.Tk()
        # 窗口大小
        self.root.geometry('600x500+300+150')
        # 固定窗口
        self.root.resizable(width=False, height=False)
        # 窗口标题
        self.root.title('学生信息管理系统')

    # 弹窗-提示
    def success(self, msg='成功！'):
        """
        :param msg: 弹窗里的文字, 默认是成功!
        :type msg: str
        """

        tkinter.messagebox.showinfo('提示', msg, parent=self.root)

    # 弹窗-错误
    def fail(self, msg='错误！'):
        """
        :param msg: 弹窗里的文字, 默认是 错误!
        :type msg: str
        """

        tkinter.messagebox.showerror('错误', msg, parent=self.root)

    # 弹窗-警告
    def warning(self, msg='警告！'):
        """
        :param msg: 弹窗里的文字, 默认是 警告！
        :type msg: str
        """

        tkinter.messagebox.showwarning('警告', msg, parent=self.root)

    # 页面-标签标题
    def label_title(self, text, padx, pady, columnspan=2):
        """
        :param text: 标签文本
        :param padx: 左右边距
        :param pady: 上下边距
        :param columnspan: 横跨的列数 默认-2
        :type text: str
        :type padx: int
        :type pady: int
        :type columnspan: int
        """

        self.label_title = tkinter.Label(self.root, text=text, font=('黑体', 24))
        self.label_title.grid(row=0, columnspan=columnspan, padx=padx, pady=pady)

    # 页面-标签
    def label(self, name, text, row, column=None, sticky=tkinter.E, font_size=14, padx=None, pady=None):
        """
        :param name: 标签名
        :param text: 文本名
        :param row: 行数
        :param column: 列数, 默认-None
        :param sticky: 紧靠左、右边, 默认值-tkinter.E
        :param font_size: 字体大小, 默认值-14
        :param padx: 左右边距, 默认-None
        :param pady: 上下边距, 默认-None
        :type name: str
        :type text: str
        :type row: int
        :type column: int
        :type sticky:
        :type font_size: int
        :type padx: int
        :type pady: int
        """

        self.label_name = self.fname('label', name)
        self.label_name = tkinter.Label(self.root, text=text, font=('宋体', font_size))
        self.label_name.grid(row=row, column=column, sticky=sticky, padx=padx, pady=pady)

    # 页面-输入框
    def entry(self, name, row, column, width=None, sticky=tkinter.W, padx=None):
        """
        :param name: 输入框名
        :param row: 行数
        :param column: 列数
        :param width: 宽, 默认-None
        :param sticky: 紧靠左、右边, 默认值-tkinter.W
        :param padx: 左右边距, 默认-None
        :type name: str
        :type row: int
        :type column: int
        :type width: int
        :type sticky:
        :type padx: int
        :return: 对象名
        """

        self.entry_name = self.fname('entry', name)
        self.entry_name = tkinter.Entry(self.root, width=width)
        if name == 'pwd':
            self.entry_name['show'] = '*'  # 隐藏显示
        self.entry_name.grid(row=row, column=column, sticky=sticky, padx=padx)
        return self.entry_name

    # 页面-组合按钮
    def frame_button(self, name1, name2, text1, text2, width=10, height=None,
                     btn1_command=None, btn2_command=None,
                     column=0, padx=40,
                     row=3, columnspan=2, pady=60):
        """
        :param name1: 按钮1名字
        :param name2: 按钮2名字
        :param text1: 按钮1文本
        :param text2: 按钮2文本
        :param width: 按钮宽度, 默认-10
        :param height: 按钮高度, 默认-None
        :param btn1_command: 按钮1事件, 默认-None
        :param btn2_command: 按钮2事件, 默认-None
        :param column: 按钮列数, 默认-0
        :param padx: 按钮的左右边距, 默认-40
        :param row: 盒子的行数, 默认-3
        :param columnspan: 盒子跨的列数, 默认-2
        :param pady: 盒子的的上下边距, 默认-60
        :type name1: str
        :type name2: str
        :type text1: str
        :type text2: str
        :type width: int
        :type height: int
        :type btn1_command:
        :type btn2_command:
        :type column: int
        :type padx: int
        :type row: int
        :type columnspan: int
        :type pady: int
        """

        self.btn1 = self.fname('button', name1)
        self.btn2 = self.fname('button', name2)

        self.frame_btn = tkinter.Frame(self.root)

        self.btn1 = tkinter.Button(self.frame_btn, text=text1, width=width, height=height,
                                   command=btn1_command)
        self.btn1.grid(row=0, column=column, padx=padx)

        self.btn2 = tkinter.Button(self.frame_btn, text=text2, width=width, height=height,
                                   command=btn2_command)
        self.btn2.grid(row=0, column=column+1, padx=padx)

        self.frame_btn.grid(row=row, columnspan=columnspan, pady=pady)

    # 页面-按钮
    def button(self, name, text, width=24, height=None, font_size=12, command=None,
               row=1, column=None, sticky=None, padx=None, pady=10):
        """
        :param name: 按钮名
        :param text: 文本名
        :param width: 宽
        :param height: 高
        :param font_size: 字体大小
        :param command: 按钮事件
        :param row: 行
        :param column: 列
        :param sticky: 紧靠左、右边, 默认值-tkinter.E
        :param padx: 左右边距
        :param pady: 上下边距
        :type name: str
        :type text: str
        :type width: int
        :type height: int
        :type font_size: int
        :type command:
        :type row: int
        :type column: int
        :type sticky:
        :type padx: int
        :type pady: int
        """

        self.btn_name = self.fname('button', name)
        self.button_add = tkinter.Button(self.root, text=text, width=width, height=height,
                                         font=('黑体', font_size), command=command)
        self.button_add.grid(row=row, column=column, sticky=sticky, padx=padx, pady=pady)

    # 页面-列表
    def treeview(self, row, columnspan):
        """
        :param row: 行数
        :param columnspan: 跨越行数
        :type row: int
        :type columnspan: int
        """
        self.dataTreeview = ttk.Treeview(self.root, show='headings', column=('sid', 'name', 'phone', 'address'))
        self.dataTreeview.column('sid', width=120, anchor="center")
        self.dataTreeview.column('name', width=120, anchor="center")
        self.dataTreeview.column('phone', width=120, anchor="center")
        self.dataTreeview.column('address', width=120, anchor="center")

        self.dataTreeview.heading('sid', text='学号')
        self.dataTreeview.heading('name', text='名字')
        self.dataTreeview.heading('phone', text='年龄')
        self.dataTreeview.heading('address', text='班级')

        self.dataTreeview.grid(row=row, columnspan=columnspan)

    # 名字处理
    def fname(self, prefix, name):
        """
        :param prefix: 前缀
        :param name: 名字
        :type prefix: str
        :type name: str
        :return: 拼接的变量名
        """

        dic = {'name': f'self.{prefix}_{name}'}
        for key in dic.keys():
            setattr(self, key, dic[key])
        print(self.name)
        return self.name

    # 查询学号是否重复
    def select_no(self, sno, bool=True):
        """
        :param sno: 学号
        :param bool: 布尔值, 默认值-True
        :type sno: int
        :type bool: bool
        """

        result = HandleMysql().select(sno)
        if not result:
            if bool:
                self.warning('学号不存在！')

    # 空值检测
    def none_value(self, data):
        """
        :param data: 列表数据
        :type data: list
        :return: True or False
        """

        flag = True
        if data[0] == '':
            self.warning('学号不能为空！')
        elif data[1] == '':
            self.warning('名字不能为空！')
        elif data[2] == '':
            self.warning('年龄不能为空！')
        elif data[3] == '':
            self.warning('班级不能为空！')
        else:
            flag = False
        return flag

    # 显示数据列表
    def show(self):
        """ treeview 显示数据 """

        self.treeview_empty(self.dataTreeview)
        list = HandleMysql().student_list()
        for item in list:
            self.dataTreeview.insert("", 1, text="line1", values=item)

    # 清空数据列表
    def treeview_empty(self, tree):
        """ treeview 清空数据 """

        x = tree.get_children()
        for item in x:
            tree.delete(item)


# if __name__ == '__main__':
#     base = BaseView()
#     base.success()
#     base.fail()
#     base.warning()
#     base.select_no(1006)
