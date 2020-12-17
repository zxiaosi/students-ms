# @Time : 2020/12/13 17:26
# @Author : 小四先生
# @File : InitializeDB.py
# @Version : 3.0
# @Description : 初始化mysql(创建、插入默认数据)
import pymysql.cursors

from lib.ConnectDB import ConnMysql


class InitMysql(ConnMysql):
    """ 初始化数据库的类 """

    def __init__(self):
        super().__init__()
        self.conn_mysql()

    # 创建数据库
    def create_database(self):
        """ 创建数据库: students """

        # 如果数据库已经存在，那么删除后重新创建
        self.cursor.execute("drop database if exists students")
        sql = "create database students"
        self.cursor.execute(sql)
        print('创建数据库成功！')

    # 创建数据库表
    def create_table(self):
        """ 创建数据表: t_student、t_user """

        # 如果数据表已经存在，那么删除后重新创建
        self.cursor.execute("drop table if exists t_student")
        self.cursor.execute("drop table if exists t_user")

        sql1 = """
            create table t_student(
                sno int primary key comment '学号',
                sname char(45) not null comment '姓名',
                sage char(45) comment '年龄',
                sclass char(45) comment '班级'
            )
        """

        sql2 = """
            create table t_user(
                user char(45) primary key comment '用户名',
                password char(45) not null comment '密码'
            )
        """

        self.cursor.execute(sql1)
        self.cursor.execute(sql2)
        print('创建数据库表成功！')

    # 插入默认数据
    def insert_data(self):
        """ 向 t_student、t_user 表中插入默认数据 """

        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL得到结果
                sql1 = """
                    insert into t_student 
                    values 
                    (1001, '张三', '20', 'Python班'),
                    (1002, '李四', '21', 'Python班'),
                    (1003, '王五', '19', 'Python班')
                """

                sql2 = """
                        insert into t_user 
                        values 
                        ('admin', 'admin')
                    """

                result1 = cursor.execute(sql1)
                result2 = cursor.execute(sql2)
                if result1 and result2:
                    print('添加数据成功！')
                self.conn.commit()
        except pymysql.MySQLError as error:
            print(error)
            # 操作失败执行回滚
            self.conn.rollback()
        finally:
            # 关闭连接释放资源
            self.cursor.close()
            self.conn.close()


# if __name__ == '__main__':
#     init = InitMysql()
#
#     init.create_database()
#
#     init.create_table()
#
#     init.insert_data()
