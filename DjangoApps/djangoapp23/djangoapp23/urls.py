
from django.contrib import admin
from django.urls import path
from app1.views import composemail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', composemail, name = 'composemail'),
]