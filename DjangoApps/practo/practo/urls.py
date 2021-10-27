from django.conf.urls import url

from doctor.views import doctorv
from clinic.views import clinicv
from patient.views import patientv

urlpatterns = [
    url(r'$^',doctorv),
    url(r'doctor/', doctorv,name='doctorhl'),
    url(r'clinic/', clinicv,name='clinichl'),
    url(r'patient/', patientv,name='patienthl'),
]
