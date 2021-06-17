# StudentsMS

### 介绍

Python-Tk模块实现学生后台管理系统

### 软件架构

软件架构说明

![](https://gitee.com/zxiaosi/image/raw/master/Project/Python/StudentMS/studentMS.png)

### 安装教程

#### 1. 配置 Python3.6 (及以上)的虚拟环境

#### 2. 安装所需的包

```python
pip install -r requirements.txt
```

### 使用说明

#### 1. 文件目录

```sh
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
		|-- connect.py			# 连接数据库
	|-- base.py					# 父类模板
|-- log							# 日志文件夹
|-- main.py						# 主程序
```

#### 2. 配置数据库信息

+ 在 `config.ini ` 中配置数据库的参数

#### 3. 运行

+  `main.py ` 运行主程序
+ 登录时会检测数据库的连接是否正常
  + 通过弹窗反馈给用户（弹窗默认3秒关闭）
  + 如果配置信息有误（弹窗弹出的时间变长）
+ 数据连接正常会进入到登录页面

### 4. 登录

+ 账号：    `admin`
+ 密码：    `admin`

### 效果演示

#### 1. 查询所有学生

![](https://gitee.com/zxiaosi/image/raw/master/Project/Python/StudentMS/all.gif)

#### 2. 添加学生信息

![](https://gitee.com/zxiaosi/image/raw/master/Project/Python/StudentMS/add.gif)

#### 3. 查询学生信息

![](https://gitee.com/zxiaosi/image/raw/master/Project/Python/StudentMS/select.gif)

#### 4. 删除学生信息

![](https://gitee.com/zxiaosi/image/raw/master/Project/Python/StudentMS/delete.gif)

#### 5. 修改学生信息

![](https://gitee.com/zxiaosi/image/raw/master/Project/Python/StudentMS/update.gif)