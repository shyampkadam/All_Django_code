from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response
from .models import Student,Employee
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework import viewsets

#ModelViewSet With DefaultRouter
class StudentModelViewSet(viewsets.ModelViewSet):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer
 authentication_classes = [BasicAuthentication]
 permission_classes = [AllowAny]

class EmployeeModelViewSet(viewsets.ModelViewSet):
 queryset = Employee.objects.all()
 serializer_class = EmployeeSerializer
 authentication_classes = [BasicAuthentication]
 permission_classes = [AllowAny]

''''
#ViewSet With DefaultRouter

class StudentViewSet(viewsets.ViewSet):
 def list(self, request):
  stu = Student.objects.all()
  serializer = StudentSerializer(stu, many=True)
  return Response(serializer.data)

 def retrieve(self, request, pk=None):
  id = pk
  if id is not None:
   stu = Student.objects.get(id=id)
   serializer = StudentSerializer(stu)
   return Response(serializer.data)

 def create(self, request):
  serializer = StudentSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def update(self,request, pk):
  id = pk
  stu = Student.objects.get(pk=id)
  serializer = StudentSerializer(stu, data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Complete Data Updated'})
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def partial_update(self,request, pk):
  id = pk
  stu = Student.objects.get(pk=id)
  serializer = StudentSerializer(stu, data=request.data, partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Partial Data Updated'})
  return Response(serializer.errors)

 def destroy(self,request, pk):
  id = pk
  stu = Student.objects.get(pk=id)
  stu.delete()
  return Response({'msg':'Data Deleted'})

'''

#9 APIViews classes
'''
class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentListCreate(ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
'''

#Code2 : 2 mixin classes
'''
class StudentCreateList(GenericAPIView, ListModelMixin,CreateModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def get(self, request, *args, **kwargs):
  return self.list(request, *args, **kwargs)
 def post(self, request, *args, **kwargs):
  return self.create(request, *args, **kwargs)

class StudentRetriveUpdateDelete(GenericAPIView,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def get(self, request, *args, **kwargs):
  return self.retrieve(request, *args, **kwargs)

 def put(self, request, *args, **kwargs):
  return self.update(request, *args, **kwargs)

 def delete(self, request, *args, **kwargs):
  return self.destroy(request, *args, **kwargs)
'''
#Code1 : 5 mixin classes
'''
class StudentList(GenericAPIView, ListModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def get(self, request, *args, **kwargs):
  return self.list(request, *args, **kwargs)

class StudentCreate(GenericAPIView, CreateModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def post(self, request, *args, **kwargs):
  return self.create(request, *args, **kwargs)

class StudentRetrive(GenericAPIView, RetrieveModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def get(self, request, *args, **kwargs):
  return self.retrieve(request, *args, **kwargs)

class StudentUpdate(GenericAPIView, UpdateModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def put(self, request, *args, **kwargs):
  return self.update(request, *args, **kwargs)

class StudentDestroy(GenericAPIView, DestroyModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def delete(self, request, *args, **kwargs):
  return self.destroy(request, *args, **kwargs)

'''