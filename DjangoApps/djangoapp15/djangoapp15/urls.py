from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import app1.views
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url('v1/', app1.views.sayHi1),
    url('v2/', app1.views.sayHi2),

    url('v3/', app1.views.Hello1.as_view()),
    url('v4/', app1.views.Hello2.as_view()),
    url('v5/', app1.views.ShowAllBooks.as_view()),

]
