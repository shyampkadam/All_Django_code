from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True)
    author = models.CharField(max_length=200, null=True)
    isbn=models.CharField(max_length=20)
    storename=models.CharField(max_length=20)