
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('showallemp/',views.showallemployeesinjsonformat),
    path('showemp/<int:pk>',views.showoneemployeesinjsonformat)
]
