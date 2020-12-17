# @Time : 2020/12/13 20:22 
# @Author : 小四先生
# @File : HandleDB.py
# @Version : 3.0
# @Description : 数据库的增删改查
import pymysql

from lib.ConnectDB import ConnMysql


def try_except(func):
    """ 异常装饰器 """

    def decorator(self, *args, **keyargs):
        try:
            return func(self, *args, **keyargs)
        except pymysql.MySQLError as error:
            print(error)
            # 操作失败执行回滚
            self.conn.rollback()
        finally:
            # 关闭连接释放资源
            self.cursor.close()
            self.conn.close()

    return decorator


class HandleMysql(ConnMysql):
    """ 数据库的增删改查 """

    def __init__(self):
        super().__init__()
        self.conn_mysql()

    # 查看学号是否存在
    @try_except
    def select(self, sno):
        """
        :param sno: 学号
        :type sno: int
        :return: 1-找到相同的学号   0-没有找到
        """

        # 获取游标对象
        with self.conn.cursor() as cursor:
            # 查找
            result = cursor.execute('select sno from t_student where sno=%s', (sno,))
            if result:
                print('找到相同的学号！')
            else:
                print('没有找到！')
            return result

    # 添加学生信息
    @try_except
    def add_student(self, sno, sname, sage, sclass):
        """
        :param sno: 学号
        :param sname: 姓名
        :param sage: 年龄
        :param sclass: 班级
        :type sno: int
        :type sname: str
        :type sage: str
        :type sclass: str
        """

        # 获取游标对象
        with self.conn.cursor() as cursor:
            # 执行SQL得到结果
            sql = "insert into t_student values (%s, %s, %s, %s)"
            result = cursor.execute(sql, (sno, sname, sage, sclass))
            if result:
                print('添加成功')
            # 操作成功执行提交
            self.conn.commit()

    # 查找学生信息
    @try_except
    def select_student(self, sno):
        """
        :param sno: 学号
        :type sno: int
        :return: 学号sno所对应的学生信息
        """

        # 获取游标对象
        with self.conn.cursor() as cursor:
            # 执行SQL得到结果
            cursor.execute('select sno, sname, sage, sclass from t_student where sno=%s', (sno,))
            result = cursor.fetchone()
            print(result)
            # 操作成功执行提交
            self.conn.commit()
            return result

    # 删除学生信息
    @try_except
    def delete_student(self, sno):
        """
        :param sno: 学号
        :type sno: int
        """

        # 获取游标对象
        with self.conn.cursor() as cursor:
            # 执行SQL得到结果
            result = cursor.execute('delete from t_student where sno=%s', (sno,))
            if result:
                print('删除成功')
            # 操作成功执行提交
            self.conn.commit()

    # 查看所有学生信息
    @try_except
    def student_list(self):
        """
        :return: 所有学生信息
        """

        # 获取游标对象
        with self.conn.cursor() as cursor:
            # 执行SQL得到结果
            cursor.execute('select sno, sname, sage, sclass from t_student')
            result = cursor.fetchall()
            # 操作成功执行提交
            self.conn.commit()
            return result

    # 更新学生信息
    @try_except
    def update_student(self, nsno, sname, sage, sclass, osno):
        """
        :param nsno: 学号(新)
        :param sname: 姓名
        :param sage: 年龄
        :param sclass: 班级
        :param osno: 学号(旧)
        :type nsno: int
        :type sname: str
        :type sage: str
        :type sclass: str
        :type osno: int
        """

        # 获取游标对象
        with self.conn.cursor() as cursor:
            # 执行SQL得到结果
            sql = "update t_student set sno=%s, sname=%s, sage=%s, sclass=%s where sno=%s"
            result = cursor.execute(sql, (nsno, sname, sage, sclass, osno))
            if result:
                print('更新成功')
            # 操作成功执行提交
            self.conn.commit()

    # 查找管理员信息
    @try_except
    def select_user(self):
        """
        :return: user与password组成的元组
        """

        # 获取游标对象
        with self.conn.cursor() as cursor:
            # 执行SQL得到结果
            cursor.execute('select user, password from t_user')
            result = cursor.fetchone()
            # 操作成功执行提交
            self.conn.commit()
            return result


# if __name__ == '__main__':
#     handle = HandleMysql()
#
#     result = handle.select(1001)
#     print(result)
#
#     handle.add_student(10011, '小六', '20', '小四班')
#
#     handle.select_student(10011)
#
#     handle.delete_student(10011)
#
#     result = handle.student_list()
#     print(result)
#
#     handle.update_student(10012, '小六', '20', '小四班', 1001)
#
#     result = handle.select_user()
#     print(result)

