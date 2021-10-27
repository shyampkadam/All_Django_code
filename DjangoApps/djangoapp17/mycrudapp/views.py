from django.shortcuts import render,redirect
from mycrudapp.models import Students
from mycrudapp.forms import StudentsForm
def insert(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = StudentsForm()
    return render(request, 'home.html', {'form': form})
def show(request):
    student=Students.objects.all()
    return render(request,'show.html', {'student':student})
def delete(request,id):
    student = Students.objects.get(id=id)
    student.delete()
    return redirect("/show")
def edit(request,id):
    student = Students.objects.get(id=id)
    form = StudentsForm(instance=student)
    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/show')
    return render(request, 'edit.html', {'form': form})