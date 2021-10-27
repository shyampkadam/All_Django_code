from django.shortcuts import render


def homev(request):
    return render(request,'home.html')
def aboutv(request):
    return render(request,'about.html')
def contactv(request):
    return render(request,'contact.html')