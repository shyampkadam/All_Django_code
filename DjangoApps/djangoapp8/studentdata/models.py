from django.db import models

# Create your models here.
class Student(models.Model):
    fullName=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    age=models.IntegerField()
    percentage=models.FloatField(default=0.0)
    def __str__(self):
        return self.fullName+','+self.city+','+str(self.age)
