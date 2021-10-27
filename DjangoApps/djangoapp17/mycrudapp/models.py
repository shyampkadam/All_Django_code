from django.db import models
class Students(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    marks= models.IntegerField()
    def __str__(self):
        return self.name+','+self.email+','+self.address+','+str(self.marks)
    class Meta:
        db_table = "Students"