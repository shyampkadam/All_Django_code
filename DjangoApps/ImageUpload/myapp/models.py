from django.db import models

# Create your models here.
class Image(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to="myimages")

class Person(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="myimages")
    class Meta:
        db_table='Person'