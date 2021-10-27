from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from empdata.models import Employee
# Create your views here.
def homev(request):
    return render(request,'emphome.html')

def empregv(request):
    return render(request,'empsignup.html')

def empregprocess(request):
    #1.Get data from html form
    v1 = request.GET.get('n1')
    v2 = request.GET.get('n2')
    v3 = request.GET.get('n3')
    v4 = request.GET.get('n4')
    v5 = request.GET.get('n5')
    #2.Prepare Employee model object
    emp1=Employee(email=v1,password=v2,fullName=v3,city=v4,salary=v5)
    try:
        emp=Employee.objects.get(email=v1)
        msg="Email is already exist & Please try with another"
        return render(request, 'empregerror.html', {'key1': msg})
    except ObjectDoesNotExist:
        emp1.save()
        msg = "Hey,"+v3+": Your reg done successfully"
        return render(request, 'empregsuccess.html', {'key1': msg})

def showallempv(request):
    employees=Employee.objects.all()
    return render(request, 'showallemp.html', {'emps': employees})

def showoneempformv(request):
    return render(request, 'showoneemp.html')

def searchemp(request):
    # 1.Get emailid from html form
    formEmail=request.GET.get('n1')
    # 2.Check emailid is there in db or not
    # 3.Prepare response
    try:
        ob1 = Employee.objects.get(email=formEmail)
        return render(request, 'empshow.html',{'e':ob1})
    except ObjectDoesNotExist:
        return render(request, 'empnotfound.html',{'mail':formEmail})

def updateempformv(request):
    return render(request, 'updateempform.html')
def updateprocess(request):
    # 1.Get emailid from html form
    formEmail = request.GET.get('n1')
    # 2.Check emailid is there in db or not
    # 3.Prepare response
    try:
        ob1 = Employee.objects.get(email=formEmail)
        return render(request, 'empedit.html', {'e': ob1})
    except ObjectDoesNotExist:
        return render(request, 'empnotfound.html', {'mail': formEmail})

def editprocess(request):
    # 1.Get data from html form
    v1 = request.GET.get('n1')
    v2 = request.GET.get('n2')
    v3 = request.GET.get('n3')
    v4 = request.GET.get('n4')
    v5 = request.GET.get('n5')
    # 2.Prepare Employee model object
    emp1 = Employee(email=v1, password=v2, fullName=v3, city=v4, salary=v5)
    emp1.save()
    return render(request, 'empshow.html',{'e':emp1})

def deleteempformv(request):
    return render(request, 'deleteempform.html')
def deleteprocess(request,n1):
    # 1.Get emailid from html form
    #formEmail = request.GET.get('n1')
    # 2.Check emailid is there in db or not
    # 3.Prepare response
    try:
        print('n1=',str(n1))
        ob1 = Employee.objects.get(email=str(n1))
        ob1.delete()
        employees = Employee.objects.all()
        return render(request, 'showallemp.html', {'emps': employees})
    except ObjectDoesNotExist:
        return render(request, 'empnotfound.html', {'mail': str(n1)})

def emploginv(request):
    return render(request,'empsignin.html')

def emploginprocess(request):
    v1 = request.GET.get('n1')
    v2 = request.GET.get('n2')
    try:
        emp=Employee.objects.get(email=v1,password=v2)
        msg=emp.fullName+", Your login done"
        return render(request, 'emploginsuccess.html', {'key1': msg})
    except ObjectDoesNotExist:
        msg = "Invalid mailid or password"
        return render(request, 'emploginerror.html', {'key1': msg})