from django.http import HttpResponse
def view1(request):
    return HttpResponse('<h1>WELCOME to View2 from App2</h1>')