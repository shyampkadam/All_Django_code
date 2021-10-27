from django.conf.urls import url
from app1.views import home_v,page1_v,page2_v,page3_v
urlpatterns = [
    url(r'$^',home_v),
    url(r'home/',home_v,name='homel'),
    url(r'page1/', page1_v, name='page1l'),
    url(r'page2/', page2_v, name='page2l'),
    url(r'page3/', page3_v, name='page3l'),
]
