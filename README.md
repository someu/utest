# UTest

# 简介

使用flask+vue实现的UI自动化测试平台。

# 开发

首先拉取项目：

```bash
git clone git@github.com:someu/utest.git
```

项目目录结构为：

```bash
.
├── README.md
├── server
└── ui
```

server目录为后端代码，ui目录为前端代码，下面说一下前后端开发的方式。

## 前端

前端基于vue3和element plus进行开发，src目录下为前端代码：

```bash
.
├── App.vue
├── api 				# 存放接口文件
├── assets 			# 存放图片、css等资源文件
├── components 	# 组件
├── router			# 路由定义
├── store				# vue store
├── util				# 工具方法
└── views				# 页面
```

安装依赖：

```bash
npm i
```

启动项目：

```bash
npm run serve
```

打包项目，输出目录为 dist 文件夹：

```bash
npm run build
```

## 后端

后端基于flask开发，app目录下为代码目录。

```bash
├── account					# 账户模块
├── config.py				# 配置文件
├── decorators.py		# 装饰器
├── email.py		
├── error						# 错误处理模块
└── models					# 数据库model定义
```

1. 安装和配置数据库

   后端使用的数据库为 mysql 和 redis，可以通过docker-compose来启动数据库。本地需要配置数据库的密码，在.env文件中配置数据库密码。

   ```yaml
   REDIS_PASS=<redis_pass>
   MYSQL_PASS=<mysql_pass>
   ```

   启动数据库：

   ```bash
   docker-compose up -d
   ```

2. 安装python虚拟环境和依赖

   建议使用conda管理python虚拟环境和依赖：

   ```bash
   # 创建虚拟环境
   conda create utest python=3.6
   # 激活虚拟环境
   conda activate utest
   # 安装依赖
   pip install -r requirements.txt
   ```

3. 修改配置

   项目的配置在config.env文件中，修改数据库的密码和地址：

   ```
   ADMIN_PASSWORD=utest@utest.com
   ADMIN_EMAIL=xxz&ppz@1314
   REDIS_URL=http://<redis_pass>@<redis_ip>:16379
   DATABASE_URL=mysql+pymysql://root:<mysql_pass>@<mysql_ip>:13306/utest
   SECRET_KEY=WHvGRP9LUFKkC5HpXi
   ```

4. 生成模拟数据

   ```bash
   # 重置数据库
   python3 manage.py recreate_db
   # 生成通用的数据，例如权限表，会插入超级管理员用户，admin的邮箱和密码在第三步的配置中填写
   python3 manage.py setup_general
   # 生成模拟数据，例如模拟用户等
   python3 manage.py add_fake_data
   ```

5. 启动服务

   ```bash
   python manage.py runserver
   ```

# 部署