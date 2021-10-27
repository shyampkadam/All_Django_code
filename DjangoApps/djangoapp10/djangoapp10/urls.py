from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from emp.views import homev
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'$^',homev),
  ]