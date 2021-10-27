from django.shortcuts import render

from empdata.forms import EmpSignInForm

def homev(request):
    if request.method=='POST':
        form=EmpSignInForm(request.POST)
        if form.is_valid():
            print('Form Validation is Done')
            print('Your full name is:',form.cleaned_data['fullName'])
            print('Your age is:', form.cleaned_data['age'])
            print('Your city is:', form.cleaned_data['city'])
            print('Your email is:', form.cleaned_data['email'])
            print('Your password is:', form.cleaned_data['password'])
            print('Your address is:', form.cleaned_data['address'])
    form=EmpSignInForm()
    return  render(request,'signin.html',{'form':form})