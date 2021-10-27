
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.insert, name='insert'),
    path('show/', views.show, name='show'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)