from django.db import models
class Doctor(models.Model):
    fullName    =models.CharField(max_length=30)
    mobileNumber=models.IntegerField()
    password    =models.CharField(max_length=20)
    exp         =models.IntegerField()
    def __str__(self):
        return self.fullName+','+str(self.mobileNumber)+','+self.password+','+str(self.exp)
