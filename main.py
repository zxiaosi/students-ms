# @Time : 2020/12/14 11:01 
# @Author : 小四先生
# @File : main.py
# @Version : 1.0
# @Description : 主函数
from db.HandleDB import HandleMysql
from view.index.index import Index

if __name__ == '__main__':
    index = Index()
    index.index_view()

