from django.db import models
class Book(models.Model):
    name=models.CharField(max_length=10)
    nop=models.IntegerField()
    cost=models.FloatField()
    def __str__(self):
        return self.name
    class Meta:
        db_table='book'