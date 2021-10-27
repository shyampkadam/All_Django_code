from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student,Employee
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer
 permission_classes = [IsAuthenticated]

class EmployeeModelViewSet(viewsets.ModelViewSet):
 queryset = Employee.objects.all()
 serializer_class = EmployeeSerializer
 authentication_classes = [BasicAuthentication]
 permission_classes = [IsAuthenticated]
