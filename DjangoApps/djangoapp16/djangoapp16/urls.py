from django.conf.urls import url,include
urlpatterns = [
    url(r'app1/',include('app1.urls')),
    url(r'app2/',include('app2.urls')),
    url(r'app3/',include('app3.urls')),
]
