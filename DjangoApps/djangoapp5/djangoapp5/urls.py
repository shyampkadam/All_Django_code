from django.conf.urls import url

from .views import home_view,process_view


urlpatterns = [
    url(r'$^',home_view),
    url(r'home/', home_view,name='homel'),
    url(r'process/', process_view,name='processl'),
]
