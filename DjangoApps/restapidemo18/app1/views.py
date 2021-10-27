from django_filters.rest_framework import DjangoFilterBackend

from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
class StudentList(ListAPIView):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer
 filterset_fields = ['city']
