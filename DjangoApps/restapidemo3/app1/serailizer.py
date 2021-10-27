from rest_framework import serializers
from app1.models import Employee
class EmployeeSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    fullName=serializers.CharField(max_length=40)
    city=serializers.CharField(max_length=40)
    salary=serializers.FloatField(default=0.0)
    #This method gets called when we do is_valid() & data stored into DB
    def create(self,validate_data):
        return Employee.objects.create(**validate_data)