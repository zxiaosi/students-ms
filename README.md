# StudentsMS

#### 介绍
Python-Tk模块实现学生后台管理系统

#### 软件架构
软件架构说明

![学生信息管理系统](https://gitee.com/zxiaosi/img/raw/master/Python/学生信息管理系统.png)


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
	|-- LogDB.py				# 日志
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
|-- log							# 日志文件夹
|-- main.py						# 主程序
```

1.  配置数据库信息
    + 在 `config.ini ` 中配置数据库的参数
2.  运行
    +  `main.py ` 运行主程序
    + 登录时会检测数据库的连接是否正常
      + 通过弹窗反馈给用户（弹窗默认3秒关闭）
      + 如果配置信息有误（弹窗弹出的时间变长）
    + 数据连接正常会进入到登录页面
3.  登录
    + 账号：    `admin`
    + 密码：    `admin`
