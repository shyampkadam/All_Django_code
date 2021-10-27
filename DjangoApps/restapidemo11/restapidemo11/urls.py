from rest_framework.authtoken.views import obtain_auth_token 
from django.contrib import admin
from django.urls import path,include
from app1 import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('studentapi', views.StudentModelViewSet, basename='student')
router.register('employeeapi', views.EmployeeModelViewSet, basename='employee')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token-auth/', obtain_auth_token, name='api_token_auth'), 
]
