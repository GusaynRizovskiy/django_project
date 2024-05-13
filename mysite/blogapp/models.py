from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=40)

class Teg(models.Model):
    name = models.CharField(max_length=20)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Teg)
