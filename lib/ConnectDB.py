# @Time : 2020/12/13 21:47 
# @Author : 小四先生
# @File : ConnectDB.py
# @Version : 1.0
# @Description : 连接数据库
import pymysql

from lib.readconfig import ReadConfig


class ConnMysql(object):
    """ 连接数据库的类 """

    def __init__(self):
        self.data = ReadConfig()

    # 数据库连接
    def conn_mysql(self):
        """
        :return: True-连接数据库成功  False-连接数据库失败
        """
        host = self.data.get_db("host")
        port = self.data.get_db("port")
        user = self.data.get_db("user")
        password = self.data.get_db("password")
        db = self.data.get_db("db")
        charset = self.data.get_db("charset")

        try:
            self.conn = pymysql.connect(host=host,
                                        port=int(port),
                                        user=user,
                                        password=password,
                                        db=db,
                                        charset=charset)
            self.cursor = self.conn.cursor()
            print('数据库连接成功！')
            return True
        except:
            print('数据库连接失败！')
            return False

# if __name__ == '__main__':
#     conn = ConnMysql()
#     conn.conn_mysql()
