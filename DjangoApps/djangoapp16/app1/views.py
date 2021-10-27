from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    print('$$$$$$Inside view: during request processing$$$$$$')
    return HttpResponse('<h1>WELCOME to View1 from App1</h1>')

def one_v(request):
    return render(request,'one.html')

def two_v(request):
    return render(request,'two.html')