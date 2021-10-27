from django.db import models

# Abstract Base Class
class Employee(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    class Meta:
        abstract = True
#Derived class1
class RegularEmployee(Employee):
    salary=models.IntegerField()
    bonus=models.IntegerField()
    def __str__(self):
        return self.name
#Derived class2
class ContractEmployee(Employee):
    payperhour=models.IntegerField()
    duration=models.IntegerField()
    def __str__(self):
        return self.name