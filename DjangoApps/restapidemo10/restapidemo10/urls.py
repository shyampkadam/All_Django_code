from django.contrib import admin
from django.urls import path,include
from app1 import views
from rest_framework.routers import DefaultRouter
#ModelViewSet With DefaultRouter

# Creating Router Object
router = DefaultRouter()
# Register StudentModelViewSet with Router
router.register('studentapi', views.StudentModelViewSet, basename='student')
# Register EmployeeModelViewSet with Router
router.register('employeeapi', views.EmployeeModelViewSet, basename='employee')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]


#ViewSet With DefaultRouter
'''
router.register('studentapi', views.StudentViewSet, basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
'''
#9 API view endpoints

# path('studentapi/', views.StudentList.as_view()),
# path('studentapi/', views.StudentCreate.as_view()),
# path('studentapi/<int:pk>/', views.StudentRetrieve.as_view()),
# path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
# path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),
# path('studentapi/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
# path('studentapi/<int:pk>/', views.StudentRetrieveDestroy.as_view()),
#path('studentapi/', views.StudentListCreate.as_view()),
#path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),


#2 mixin classes endpoints

# path('studentapi/', views.StudentCreateList.as_view()),
# path('studentapi/<int:pk>/', views.StudentRetriveUpdateDelete.as_view()),

#5 mixin classes endpoints

# path('studentapi/', views.StudentList.as_view()),
# path('studentapi/', views.StudentCreate.as_view()),
# path('studentapi/<int:pk>/', views.StudentRetrive.as_view()),
# path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
# path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),