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
