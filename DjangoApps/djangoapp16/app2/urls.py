from django.conf.urls import url
from app2.views import view1
urlpatterns = [
    url(r'v1/',view1)
]
