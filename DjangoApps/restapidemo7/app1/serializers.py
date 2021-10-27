from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    #3.Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be start with R')
    #name=serializers.CharField(read_only=True)
    name=serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        #read_only_fields=['name', 'roll']
        #extra_kwargs={'name':{'read_only':True}}
    # 1.Field Lavel Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seats are Full')
        return value
    # 2.Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        roll=data.get('roll')
        if nm.lower() == 'ravi' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data