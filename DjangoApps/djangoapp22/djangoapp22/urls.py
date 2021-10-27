from django.conf.urls import url

from app1.views import index,insertBooks
from django.contrib import admin
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'$^', index),
    url(r'save/', insertBooks),
]