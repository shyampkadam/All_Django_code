from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)


class Employee(models.Model):
    name= models.CharField(max_length=50)
    salary=models.FloatField()
    city = models.CharField(max_length=50)

