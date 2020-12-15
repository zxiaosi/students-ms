# @Time : 2020/12/14 11:01 
# @Author : 小四先生
# @File : main.py
# @Version : 1.1
# @Description : 主函数
from view.index.index import Index
from db.InitializeDB import InitMysql


if __name__ == '__main__':
    init = InitMysql()
    # init.create_database()
    init.create_table()
    init.insert_data()

    index = Index()
    index.index_view()
