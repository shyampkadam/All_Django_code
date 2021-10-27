from django.shortcuts import render

# Create your views here.
from app1.forms import Form1,Form2,Form3


def one_v(request):
    form1=Form1()
    return render(request,'one.html',{'form':form1})
def two_v(request):
    #Get name from html from
    name=request.GET.get('name')
    #Set name into session
    #request.session['key1']=name
    form1 = Form2()
    #Set name into cookie
    c1 = render(request,'two.html',{'form':form1})
    c1.set_cookie('name', name)
    return c1
def three_v(request):
    # Get city from html from
    city = request.GET.get('city')
    # Set city into session
    # request.session['key2'] = city
    form1 = Form3()
    # Set city into cookie
    c1 = render(request, 'three.html', {'form': form1})
    c1.set_cookie('city', city)
    return c1
def final_v(request):
    # Get age from html from
    personAge = request.GET.get('age')
    # Set age into session
    #request.session['key3'] = age
    # Get all cookies data from the browser & display into final.html
    personName=request.COOKIES['name']
    personCity = request.COOKIES['city']
    dict1={'k1':personName,'k2':personCity,'k3':personAge}
    c1 = render(request, 'final.html',dict1)
    # Set age into cookie
    c1.set_cookie('age', personAge)
    return c1