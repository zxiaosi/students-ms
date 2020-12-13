# @Time : 2020/12/13 21:47 
# @Author : 小四先生
# @File : ConnectDB.py
# @Version : 1.0
# @Description : 连接数据库

import pymysql

from readconfig import ReadConfig


class ConnMysql:
    def __init__(self):
        self.data = ReadConfig()

    def conn_mysql(self):
        host = self.data.get_db("host")
        port = self.data.get_db("port")
        user = self.data.get_db("user")
        password = self.data.get_db("password")
        db = self.data.get_db("db")
        charset = self.data.get_db("charset")

        self.conn = pymysql.connect(host=host,
                                    port=int(port),
                                    user=user,
                                    password=password,
                                    db=db,
                                    charset=charset)
        self.cursor = self.conn.cursor()

        print('数据库连接成功！')
