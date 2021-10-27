from django.conf.urls import url

from .views import home,about

urlpatterns = [
    url(r'$^',home),
    url(r'begin',home),
    url(r'about', about),
]

#localhost:8000
#localhost:8000/begin
#localhost:8000/about
