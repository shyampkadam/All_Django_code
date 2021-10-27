from rest_framework import serializers
class EmployeeSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    fullName=serializers.CharField(max_length=40)
    city=serializers.CharField(max_length=40)
    salary=serializers.FloatField(default=0.0)
