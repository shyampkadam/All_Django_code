from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    salary= models.FloatField()
    class Meta:
        verbose_name_plural = "employee"
        db_table='employee'
    def __str__(self):
        return self.name
class Dept(models.Model):
    name = models.CharField(max_length=200)
    empid = models.ForeignKey(Employee, default=1,on_delete=models.SET_DEFAULT)
    exp = models.CharField(max_length=200)
    class Meta:
        db_table='dept'
    def __str__(self):
        return self.name