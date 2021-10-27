from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework  import renderers


# Create your views here.
def showallemployeesinjsonformat(request):
    employeeQuerySet=Employee.objects.all()
    #print(employeeQuerySet)
    empSerializer=EmployeeSerializer(employeeQuerySet,many=True)
    #print(empSerializer)
    json_data=renderers.JSONRenderer().render(empSerializer.data)
    #print(json_data)
    return HttpResponse(json_data,content_type='application/json')

def showoneemployeesinjsonformat(request,pk):
    employeeQuerySet=Employee.objects.get(id=pk)
    empSerializer=EmployeeSerializer(employeeQuerySet)
    json_data=renderers.JSONRenderer().render(empSerializer.data)
    return HttpResponse(json_data,content_type='application/json')