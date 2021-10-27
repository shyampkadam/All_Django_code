from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from .populate import populate
class StudentList(ListAPIView):
 populate(20)
 queryset = Student.objects.all()
 serializer_class = StudentSerializer