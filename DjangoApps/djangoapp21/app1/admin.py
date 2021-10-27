from django.contrib import admin

from app1.models import Car,Engine,Movie,AudioSongs,Student,Course

admin.site.register(Student)
admin.site.register(Course)

admin.site.register(Movie)
admin.site.register(AudioSongs)
admin.site.register(Car)
admin.site.register(Engine)