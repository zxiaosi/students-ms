# @Time : 2020/12/13 17:56 
# @Author : 小四先生
# @File : readconfig.py
# @Version : 1.0
# @Description : 读取配置文件
import os
import configparser


class ReadConfig:
    """ 读取配置文件的类 """

    def __init__(self, filepath=None):
        if filepath:
            config_path = filepath
        else:
            # 配置文件所在位置
            path = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(path, "config.ini")
        # 读取配置文件
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    # 获取section名为Mysql-Database所对应的键值对
    def get_db(self, param):
        """
        :param param: config.ini中名为Mysql-Database所对应的键
        :type param: str
        :return: config.ini中名为Mysql-Database所对应的值
        """
        value = self.cf.get("Mysql-Database", param)
        return value
