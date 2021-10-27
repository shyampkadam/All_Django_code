from django.shortcuts import render

def home_view(request):
    #ABOUT  YOUR PERSONAL DETAILS
    return render(request,'home.html')

def about_view(request):
    # ABOUT YOUR EDUCATION
    return render(request,'about.html')