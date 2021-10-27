from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
# Create your views here.

class StudentList(ListAPIView):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer
 #filter_backends = [DjangoFilterBackend]
 #filterset_fields=['city','roll']
 filter_backends = [filters.SearchFilter]
 search_fields=['city',]
 '''
 def get_queryset(self):
  user = self.request.user
  return Student.objects.filter(passby=user)
 '''