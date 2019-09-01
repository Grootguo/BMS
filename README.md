# BMS
 Book management system（图书管理系统）

修改日期：2019-07-30

### 一、摘要

​		一个简单的图书管理系统包括图书馆内书籍的信息、学校在校学生的信息以及学生的借阅信息。此系统功能分为面向学生和面向管理员两部分，其中学生可以进行借阅、续借、归还和查询书籍等操作，管理员可以完成书籍和学生的增加，删除和修改以及对学生，借阅、续借、归还的确认。

### 二、需求设计

​		1.图书信息管理

​		2.学生老师图书借阅

### 三、数据库设计

​		目前已完成数据库建立

![1567351561977](C:\Users\MSI-PC\Desktop\BMS\README.assets\1567351561977.png)

```mysql
create tabel book_publish(
    nid primary key auto_increment,
    name varchar(32) not null,
    email varchar(32) not null
)
create tabel book_book(
	nid primary key auto_increment,
    title varchar(32) not null,
    price decimal(6,2) not null,
    pub_date datetime not null,
    constraint fk_publish foreign key(publish_id) references book_publish(id)
    on delete cascade
    on update cascade,
)
create tabel book_book_authors(
    id primary key auto_increment,
    constraint fk_book foreign key(book_id) references book_book(nid)
    on delete cascade
    on update cascade,
    constraint fk_author foreign key(author_id) references book_author(nid)
    on delete cascade
    on update cascade,
)
create tabel book_author(
    nid primary key auto_increment,
    name varchar(32) not null,
    age int(11) not null,
    email varchar(32) not null,
    constraint fk_authordetail foreign key(ad_id) references book_authordetail(id)
    on delete cascade
    on update cascade,
)

create table book_authordetail(
    id primary key auto_increment,
    addr varchar(32) not null,
    tel varchar(32) not null,
)

```

一般情况我采用 django 的 orm 机制创建数据库中的表

```python
from django.db import models


# Create your models here.
class Book(models.Model):
    """
    书籍表
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title


class Publish(models.Model):
    """
    出版社表
    """
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)


class Author(models.Model):
    """
    作者表
    """
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.CharField(max_length=32)
    ad = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    """
    作者地址
    """
    addr = models.CharField(max_length=32)
    tel = models.CharField(max_length=32)

```

需要还要完善的功能：学生的借阅书籍，以及老师借阅书籍，学生老师的个人信息。

### 四、主要运用的技术

前端：bootstrap、Ajax、jQuery

后端：python、Django、Mysql

可以改进，基于vue的前后端分离实现。大大提升开发效率。以及采用其他 orm 的框架。