from django.contrib import admin
from django.urls import path
from app1.views import profile_upload
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile_upload, name="profile_upload"),
]