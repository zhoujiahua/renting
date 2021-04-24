# 租房信息推荐系统

## 项目简介

使用高德地图GPS定位技术获取用户当前所在城市信息，通过Python爬虫技术采集58同城当前所在城市租房信息进行分析处理，为用户匹配附近最佳的租房信息列表。通过高德地图路线规划帮助用户规划房源信息路线。

## 技术栈

项目使用Python3、flask框架、MySql5.7数据库、Beautiful Soup爬虫框架；页面展示使用Layui、jQuery对页面进行展示以及高德地图技术等。

## 项目启动

> 虚拟环境

虚拟环境是用于依赖项管理和项目隔离的python工具，它可以将python程序和pip包管理工具安装在本地的隔离目录中（非全局安装）。

> Pipenv简介

pipenv发布于2017年1月，它是一种Python依赖管理工具，你可以把它看做是pip和virtualenv的组合体，它基于Pipfile的依赖记录方式，用于替代旧的记录方式requirements.txt。
pipenv会自动帮你管理虚拟环境和依赖文件，并且提供一系列命令和选项来帮助你实现各种依赖和环境管理相关的操作。简而言之，它更方便、完善和安全。

> 官方文档 [https://pipenv.pypa.io/en/latest/](https://pipenv.pypa.io/en/latest/)

> 基本使用 [https://www.cnblogs.com/blueberry-mint/p/13362737.html](https://www.cnblogs.com/blueberry-mint/p/13362737.html)

> Pipenv安装

`pip3 install pipenv`或`python3 -m pip install pipenv`
安装完成可以通过命令pipenv --version检测安装是否成功

> 创建环境

`pipenv install`

上述命令会生成Pipfile和Pipfile.lock，使用pipenv创建虚拟环境，自动生成一个随机的虚拟环境目录名。

如果在windows系统下执行命令，生成的虚拟环境在C:\Users\用户名\.virtualenvs文件夹下。

一般虚拟环境目录名的前缀是你创建环境时所在的项目目录名，如在myblog目录下执行命令，虚拟环境的目录名称就是myblog-Gtn4e1q9，后半部分为随机字符串。

> 激活虚拟环境

`pipenv shell`

创建环境后会自动进入到虚拟环境中，当退出虚拟环境重新进入到虚拟环境则需要执行以上命令。

> 安装依赖包到虚拟环境

`pipenv install requests`

不管是否激活虚拟环境，都可以执行`pipenv install`库名来安装。

> 查看已安装的模块

`pipenv graph`

> 卸载已经安装的模块

`pipenv uninstall requests`

> 获取当前虚拟环境位置

`pipenv --venv`

> 寻找当前项目的根目录

`pipenv --where`

> Python反向生成requirements.txt

`pip freeze > requirements.txt`

> 通过requirements.txt文件安装模块

`pipenv install -r requirements.txt`


