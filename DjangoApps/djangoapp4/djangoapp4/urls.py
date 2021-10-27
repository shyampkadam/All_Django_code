from django.conf.urls import url

from .views import home_view,about_view

urlpatterns = [
    url(r'$^', home_view),
    url(r'home/', home_view,name='homel'),
    url(r'about/', about_view,name='aboutl'),
]
#http://127.0.0.1:8000/         =  home_view
#http://127.0.0.1:8000/home     =  home_view