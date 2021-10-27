from django.shortcuts import render,redirect
from .models import Person
from.forms import PersonForm
# Create your views here.
def insert(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = PersonForm()
    return render(request, 'home.html', {'form': form})
def show(request):
    if request.method == 'GET':
        person=Person.objects.all()
        return render(request,'showdata.html',{'person':person})