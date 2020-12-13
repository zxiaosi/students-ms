# @Time : 2020/12/13 17:37 
# @Author : 小四先生
# @File : test.py
# @Version : 1.0
# @Description : 测试
from unittest import TestCase
import os
import configparser


class Test(TestCase):

    def test_config(self):
        # 配置文件路径
        path = os.getcwd()
        filename = os.path.join(path, 'config.ini')

        # 读取配置文件
        cf = configparser.ConfigParser()
        cf.read(filename)

        # 获取文件中所有的section
        # (一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])
        # ，并以列表的形式返回
        secs = cf.sections()

        # 获取某个section名为Mysql-Database所对应的键
        options = cf.options("Mysql-Database")
        print(options)

        # 获取section名为Mysql-Database所对应的全部键值对
        items = cf.items("Mysql-Database")
        print(items)

        # 获取[Mysql-Database]中host对应的值
        host = cf.get("Mysql-Database", "host")
        print(host)

    # def test_
