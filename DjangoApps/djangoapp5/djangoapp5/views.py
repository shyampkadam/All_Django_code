from django.shortcuts import render


def home_view(request):
    return render(request,'index.html')

def process_view(request):
    #1.Accept form input fields data
    personName=request.GET.get('n1')
    personAge = request.GET.get('n2')
    #2.Send above data(name & age) to process.html
    return render(request,'process.html',{'k1':personName,'k2':personAge})