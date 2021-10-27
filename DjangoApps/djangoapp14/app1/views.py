from django.http import HttpResponse
from app1.models import Employee
def empregv(request):
    emp1=Employee(email='test1@gmail.com',password='testpswd',fullName='test',city='testcity',salary=555)
    emp1.save()
    return HttpResponse('<h2>Record has been saved</h2>')