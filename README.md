---
title: Django study project

time:2017-06-03 20:52:26

---

## 1 Introduction
Learning django.

记得, 将django-source仓库代码放到该分支下.


## 2 Author
unusebamboo


## 3 Branch
### 3.1 Develop_template
> Update Time: 2017-10-23 10:00:49 

#### 3.1.1 Function
该分支主要用于系统性的学习django的template概念, 便于在使用django-bootstrap3库时
更好的应用, 从而搭建版本号为V.1.0的个人博客.

#### 3.1.2 过程
- 了解基本知识点并在代码中注释, 此类技术点没必要记录在印象笔记中
- 进行一些基本的功能测试, 没必要注重页面的美观度
- 引入 Internet 上已有的方案或者模板实例, 进行一个较为全面的应用

#### 3.1.3 模板
> 子模板的工作: 用户内容填充父模板的空block

模板三级结构如下: 
- base.html来控制主要视觉和体验
- 为站点的每一个"分支"创建一个base_sectionname.html模板, 例如base_sports.html, 这些包含自己特定的样式
- 每一种页面类型对应上面的分支模板

继承:
- extend必须在首行
- 尽可能在base.html设置尽可能多的block

#### 3.1.4 知识点
- 模板系统并非简单的将Python嵌入到 HTML 中, 设计理念: 致力于表现外观, 而不是程序逻辑
- 模板是纯文本文件
- 模板包含: 变量--使用时会被值替换, 标签--控制模板逻辑
- 自定义标签和过滤器库: 例如staticfiles, 需要使用load进行加载, 并且不能继承给孙模板

#### 3.1.5 使用(python)
面向python程序员, 使用模板, 参考: [模板语言](http://python.usyiyi.cn/documents/django_182/ref/templates/api.html)

## 4 Directory
### 4.1 django
链接django 1.2源码, 其中[源码注释版](git@github.com:unlessbamboo/django-source.git), 
注意, 该注释版删除了源码中所有的locale, html等静态文件.

























