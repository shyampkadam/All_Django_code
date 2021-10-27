from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_v(request):
    return render(request,'home.html')
def page1_v(request):
    #Get data from html form
    personName=request.GET.get('n1')
    #Set personName into session
    #request.session['namek']=personName
    #Set personName into cookie
    c1 = render(request,'page1.html',{'name':personName})
    c1.set_cookie('name',personName,max_age=60)
    return c1
def page2_v(request):
    #Get personName from session
    #personName = request.session['namek']
    # Get personName from Cookie
    personName=request.COOKIES['name']
    return render(request,'page2.html',{'name':personName})
def page3_v(request):
    # Get personName from session
    # personName = request.session['namek']
    # Get personName from Cookie
    personName = request.COOKIES['name']
    return render(request,'page3.html',{'name':personName})