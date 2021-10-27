from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from djangoapp23.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
def composemail(request):
    sub = forms.SubscribeForm()
    if request.method == 'POST':
        sub = forms.SubscribeForm(request.POST)
        subject = 'Regarding Testing Mail From Django App'
        message = 'Hope you are enjoying your Django Mail Sending Session'
        recepient = str(sub['Email'].value())
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form':sub})