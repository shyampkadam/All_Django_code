from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from app1.views import empregv
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'$^',empregv)
]
