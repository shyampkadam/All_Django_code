from django.http import HttpResponse

#Function based views
def home(request):
    msg='''<h1 style='color:green'>This is Home Page</h1>'''
    return HttpResponse(msg)
def about(request):
    msg='''<h1 style='color:red'>This is About Page</h1>'''
    return HttpResponse(msg)
def contactus(request):
    msg='''<h1 style='color:blue'>This is ContactUs Page</h1>'''
    return HttpResponse(msg)