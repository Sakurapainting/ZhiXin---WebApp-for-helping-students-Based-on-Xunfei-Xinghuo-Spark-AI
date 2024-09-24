

# 质心-一个基于讯飞星火AI的帮助学生学习的WebApp
## ZhiXin---WebApp-for-helping-students-Based-on-Xunfei-Xinghuo-Spark-AI


<br />

 
## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
  - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
  - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)

### 上手指南

前端基于Vue，后端需要本地数据库MySQL。请前往[部署](#部署)，以查看部署方式。

###### 开发前的配置要求

操作系统：
windows系统

运行依赖：
vue v3.4.21
axios v1.7.1
echarts v5.5.0
vue-router v4.3.2
python v3.11.8

###### **安装步骤**

Clone the repo

```sh
git clone https://github.com/Sakurapainting/ZhiXin---WebApp-for-helping-students-Based-on-Xunfei-Xinghuo-Spark-AI
```

### 文件目录说明



### 开发的架构 

vue v3.4.21






### 部署

#### 后端部署

##### step1  windows+R键，输入cmd，打开终端

##### step2  登录mysql，输入：
```

mysql -u root -p

```
##### 并输入您数据库密码，密码在此脚本后文 @@@ 处也应输入一遍
##### 若没下载mysql，移至官网https://www.mysql.com/cn/下载并注册用户

##### step3  创建数据库，输入：
```

DROP DATABASE IF EXISTS mydatabase;

```
        # 接着输入：
```

CREATE DATABASE xinghuo;

```

##### step4  进入数据库 输入：
```

USE xinghuo;

```

##### step5  创建数据表，输入：
```

CREATE TABLE aa (  
    id INT AUTO_INCREMENT PRIMARY KEY,  
    ask TEXT,
    answer TEXT
);

```

##### 数据库本地创建成功
##### 您或许需要
```
pip install websocket-client
```
##### 请在运行此python脚本的软件内导入此库  (eg.在pycharm的settings中






#### 前端部署

##### step1  在项目根目录下 cmd 输入：
```

cd test

```
##### step2   cmd 输入：
```

npm run dev

```

### 使用到的框架

vue v3.4.21


### 贡献者



#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

you2899047197@163.com


### 版权说明


### 鸣谢


