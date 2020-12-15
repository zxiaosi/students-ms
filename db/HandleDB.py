# @Time : 2020/12/13 20:22 
# @Author : 小四先生
# @File : HandleDB.py
# @Version : 1.0
# @Description : 数据库的增删改查
import pymysql

from lib.ConnectDB import ConnMysql


class HandleMysql(ConnMysql):
    def __init__(self):
        super().__init__()
        super().conn_mysql()

    # 查找学号是否存在
    def select(self, sno):
        # 获取游标对象
        with self.conn.cursor() as cursor:
            # 查找
            result = cursor.execute('select sno from t_student where sno=%s', (sno,))
            if result:
                print('找到相同的学号！')
                # 关闭连接释放资源
                self.conn.close()
                return 1
            else:
                print('没有找到！')
                # 关闭连接释放资源
                self.conn.close()
                return 0

    # 增加学生信息
    def add_student(self, sno, sname, sage, sclass):
        print(sno, sname, sage, sclass)
        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL得到结果
                sql = "insert into t_student values (%s, %s, %s, %s)"
                result = cursor.execute(sql, (sno, sname, sage, sclass))
                if result:
                    print('添加成功')
                # 操作成功执行提交
                self.conn.commit()
        except pymysql.MySQLError as error:
            print(error)
            # 操作失败执行回滚
            self.conn.rollback()
        finally:
            # 关闭连接释放资源
            self.cursor.close()
            self.conn.close()

    # 查找学生信息
    def select_student(self, sno):
        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL得到结果
                cursor.execute('select sno, sname, sage, sclass from t_student where sno=%s', (sno,))
                result = cursor.fetchone()
                print(result)
                # 操作成功执行提交
                self.conn.commit()
                return result
        except pymysql.MySQLError as error:
            print(error)
            # 操作失败执行回滚
            self.conn.rollback()
        finally:
            # 关闭连接释放资源
            self.conn.close()

    # 删除学生信息
    def delete_student(self, sno):
        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL得到结果
                result = cursor.execute('delete from t_student where sno=%s', (sno,))
                if result:
                    print('删除成功')
                # 操作成功执行提交
                self.conn.commit()
        except pymysql.MySQLError as error:
            print(error)
            # 操作失败执行回滚
            self.conn.rollback()
        finally:
            # 关闭连接释放资源
            self.conn.close()

    # 查看所有学生信息
    def student_list(self):
        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 3.执行SQL得到结果
                cursor.execute('select sno, sname, sage, sclass from t_student')
                list = cursor.fetchall()
                # 操作成功执行提交
                self.conn.commit()
                return list
        except pymysql.MySQLError as error:
            print(error)
            # 操作失败执行回滚
            self.conn.rollback()
        finally:
            # 关闭连接释放资源
            self.conn.close()

    # 更新学生信息
    def update_student(self, nsno, sname, sage, sclass, osno):
        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL得到结果
                sql = "update t_student set sno=%s, sname=%s, sage=%s, sclass=%s where sno=%s"
                result = cursor.execute(sql, (nsno, sname, sage, sclass, osno))
                if result:
                    print('更新成功')
                # 操作成功执行提交
                self.conn.commit()
        except pymysql.MySQLError as error:
            print(error)
            # 操作失败执行回滚
            self.conn.rollback()
        finally:
            # 关闭连接释放资源
            self.conn.close()

    # 增加管理员信息
    def add_user(self):
        name = input('请输入管理员账户：')
        password = input('请输入管理员密码：')
        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL得到结果
                result = cursor.execute("insert into t_user values (user=%s, password=%s)", (name, password))
                if result:
                    print('添加成功')
                # 操作成功执行提交
                self.conn.commit()
        except pymysql.MySQLError as error:
            print(error)
            # 操作失败执行回滚
            self.conn.rollback()
        finally:
            # 关闭连接释放资源
            self.conn.close()

    # 查找管理员信息
    def select_user(self):
        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL得到结果
                cursor.execute('select user, password from t_user')
                # for row in cursor.fetchall():
                #     print('用户账号：{0}'.format(row[0]))
                #     print('用户密码：{0}'.format(row[1]))
                #     print('-' * 20)
                for row in cursor.fetchall():
                    user = row[0]
                    password = row[1]
                # 操作成功执行提交
                self.conn.commit()
                return user, password
        except pymysql.MySQLError as error:
            print(error)
            # 操作失败执行回滚
            self.conn.rollback()
        finally:
            # 关闭连接释放资源
            self.conn.close()


if __name__ == '__main__':
    handle = HandleMysql()
    # handle.add_student()
    # handle.select_student()
    # handle.delete_student()
    # handle.student_list()
    # handle.update_student()
    # handle.add_user()

    # user, password = handle.select_user()
    # print(user, password)

    # result = handle.select(1007)
    # print(result)
    # result = handle.select_student(1002)
    # print(result)

    # list = handle.student_list()
    # print(list)

    # handle.delete_student(100)

