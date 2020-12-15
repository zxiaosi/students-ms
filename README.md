# StudentsMS

#### 介绍
Python-Tk模块实现学生后台管理系统

#### 软件架构
软件架构说明


#### 安装教程

1. 配置Python3.6(及以上)的虚拟环境

2. 安装所需的包

   ```python
   pip install -r requirements.txt
   ```

#### 使用说明

```
|-- db
	|-- HandleDB.py				# 数据库的增删改查
	|-- InitializeDB.py			# 初始化数据库
|-- image
|-- lib
	|-- config.ini				# 数据库的配置文件
	|-- readconfig.py			# 读取配置文件
	|-- ConnectDB.py			# 数据库的连接文件
|-- view
	|-- admin
		|-- v_admin.py			# 管理员界面
		|-- admin_append.py		# 添加学生界面
		|-- admin_show.py		# 查找学生界面
		|-- admin_delete.py		# 删除学生界面
		|-- admin_modify.py		# 修改学生界面
		|-- admin_showAll.py	# 所有学生界面
	|-- index
		|-- index.py			# 登录界面
|-- main.py						# 主程序
```

1.  `config.ini `	配置数据库信息
2.  `main.py `	运行主程序
3.  登录
    + 账号：    `123`
    + 密码：    `123`

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
