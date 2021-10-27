from django.conf.urls import url
from .myviews import home,about,contactus

urlpatterns =   [
                        url(r'$^',home),
                        url(r'about',about),
                        url(r'contact', contactus),
                        url(r'home', home),
                ]
