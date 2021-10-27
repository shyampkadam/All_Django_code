from django.conf.urls import url
from django.contrib import admin
from empdata.views import homev
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'$^',homev)
]
