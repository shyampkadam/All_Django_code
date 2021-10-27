from django.conf.urls import url
from app1.views import home_view,one_v,two_v
urlpatterns = [
    url(r'$^',home_view),
    url(r'home/',one_v,name='homel'),
    url(r'about/', two_v, name='aboutl')
]
