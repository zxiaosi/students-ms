# @Time : 2020/12/13 20:22 
# @Author : 小四先生
# @File : HandleDB.py
# @Version : 1.0
# @Description : 数据库的增删改查
import pymysql

from ConnectDB import ConnMysql


class HandleMysql(ConnMysql):
    def __init__(self):
        super().__init__()
        super().conn_mysql()

    # 增加学生信息
    def add_student(self):
        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL得到结果
                result = cursor.execute("insert into t_student values (1004, '小红', '20', 'Python班')")
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

    # 查找学生信息
    def select_student(self):
        no = int(input('要查找的学生学号：'))
        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL得到结果
                cursor.execute('select sno, sname, sage, sclass from t_student where sno=%s', (no,))
                result = cursor.fetchone()
                print(result)
                # 操作成功执行提交
                self.conn.commit()
        except pymysql.MySQLError as error:
            print(error)
            # 操作失败执行回滚
            self.conn.rollback()
        finally:
            # 关闭连接释放资源
            self.conn.close()

    # 删除学生信息
    def delete_student(self):
        no = int(input('要删除的学生学号：'))
        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL得到结果
                result = cursor.execute('delete from t_student where sno=%s', (no,))
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

    # 查看学生信息
    def student_list(self):
        try:
            # 2.获取游标对象
            with self.conn.cursor() as cursor:
                # 3.执行SQL得到结果
                cursor.execute('select sno, sname, sage, sclass from t_student')
                for row in cursor.fetchall():
                    print('编号：{0}'.format(row[0]))
                    print('学生编号：{0}'.format(row[1]))
                    print('学生成绩：{0}'.format(row[2]))
                    print('-' * 20)
        except pymysql.MySQLError as error:
            print(error)
            # 4.操作失败执行回滚
            self.conn.rollback()
        finally:
            # 5.关闭连接释放资源
            self.conn.close()

    # 更新学生信息
    def update_student(self):
        id = int(input('要编辑的学生学号: '))
        name = input('学生的新名字：')
        try:
            # 获取游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL得到结果
                result = cursor.execute('update t_student set sname=%s where sno=%s',
                                        (name, id))
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


if __name__ == '__main__':
    handle = HandleMysql()
    # handle.add_student()
    # handle.select_student()
    # handle.delete_student()
    # handle.student_list()
    # handle.update_student()

