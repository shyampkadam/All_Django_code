from django.db import models



class Student(models.Model):

    name = models.CharField(max_length=30)
    courses = models.ManyToManyField('Course', related_name='studentcourses')
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Movie(models.Model):
    name=models.CharField(max_length=10)
    year=models.IntegerField()
    rating=models.FloatField()
    def __str__(self):
        return self.name

class AudioSongs(models.Model):
    name=models.CharField(max_length=10)
    length=models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return self.name












class Car(models.Model):
	reg_no = models.CharField(max_length=10)
	owner_name = models.CharField(max_length = 100)

class Engine(models.Model):
    car = models.OneToOneField(Car,on_delete = models.CASCADE, primary_key = True)
    engine_fuel_type = models.CharField(max_length=100)
    engine_year = models.IntegerField()

