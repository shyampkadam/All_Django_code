
from django.contrib import admin
from django.urls import path
from app1 import views
import app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.handlingRequest4),
]
