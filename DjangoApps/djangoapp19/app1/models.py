from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Employee"
        db_table = 'employee'
#Derived class1
class RegularEmployee(Employee):
    salary=models.IntegerField()
    bonus=models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "RegularEmployee"
        db_table = 'regularemployee'
#Derived class2
class ContractEmployee(Employee):
    payperhour=models.IntegerField()
    duration=models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "ContractEmployee"
        db_table = 'contractemployee'

