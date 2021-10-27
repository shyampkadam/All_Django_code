from django.shortcuts import render

def home(request):
    #view data
    myname='Chanti'
    return render(request,'one.html')

def about(request):
    return render(request,'two.html')