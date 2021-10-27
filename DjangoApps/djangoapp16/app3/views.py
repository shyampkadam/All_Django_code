from django.http import HttpResponse
def view2(request):
    return HttpResponse('<h1>WELCOME to View3 from App3</h1>')