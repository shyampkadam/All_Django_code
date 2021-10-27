from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

#1.Function Based API View Code
'''
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
 if request.method == 'GET':
  id = request.data.get('id')
  if id is not None:
   stu = Student.objects.get(id=id)
   serializer = StudentSerializer(stu)
   return Response(serializer.data)

  stu = Student.objects.all()
  serializer = StudentSerializer(stu, many=True)
  return Response(serializer.data)

 if request.method == 'POST':
  serializer = StudentSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'})
  return Response(serializer.errors)

 if request.method == 'PUT':
  id = request.data.get('id')
  stu = Student.objects.get(pk=id)
  serializer = StudentSerializer(stu, data=request.data, partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Updated'})
  return Response(serializer.errors)

 if request.method == 'DELETE':
  id = request.data.get('id')
  stu = Student.objects.get(pk=id)
  stu.delete()
  return Response({'msg':'Data Deleted'})
'''
#2.Class Based API View Code
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

class StudentAPI(APIView):
 def get(self, request, pk=None, format=None):
  id = pk
  if id is not None:
   stu = Student.objects.get(id=id)
   serializer = StudentSerializer(stu)
   return Response(serializer.data)

  stu = Student.objects.all()
  serializer = StudentSerializer(stu, many=True)
  return Response(serializer.data)

 def post(self, request, format=None):
  serializer = StudentSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def put(self, request, pk, format=None):
  id = pk
  stu = Student.objects.get(pk=id)
  serializer = StudentSerializer(stu, data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Complete Data Updated'})
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def delete(self, request, pk, format=None):
  id = pk
  stu = Student.objects.get(pk=id)
  stu.delete()
  return Response({'msg':'Data Deleted'})
  