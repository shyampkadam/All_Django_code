from django.conf.urls import url
from app1.views import one_v,two_v,three_v,final_v
urlpatterns = [
    url(r'$^',one_v),
    url(r'one/',one_v,name='onel'),
    url(r'two/', two_v, name='twol'),
    url(r'three/', three_v, name='threel'),
    url(r'final/', final_v, name='finall'),
]
