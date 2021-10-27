from django.conf.urls import url
from django.contrib import admin
from empdata.views import emploginv,emploginprocess,homev,empregv,empregprocess,showallempv,showoneempformv,searchemp,updateempformv,updateprocess,editprocess,deleteempformv,deleteprocess

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'$^',homev),
    url(r'home/', homev,name='homel'),
    url(r'empreg/', empregv,name='empregl'),
    url(r'empregprocess/', empregprocess,name='empregprocessl'),
    url(r'emplogin/', emploginv, name='emploginl'),
    url(r'emploginprocess/', emploginprocess, name='emploginprocessl'),
    url(r'showallemp/',showallempv,name='showallempl'),
    url(r'showemp/',showoneempformv,name='showempl'),
    url(r'searchemp/',searchemp,name='searchemp'),
    url(r'updateempform/',updateempformv,name='updateempl'),
    url(r'updateprocess/',updateprocess,name='updateprocess'),
    url(r'editprocess/',editprocess,name='editprocess'),
    url(r'deleteempform/', deleteempformv, name='deleteempl'),
    url(r'deleteprocess/(?P<n1>\w+)/$', deleteprocess, name='deleteprocess'),
]
