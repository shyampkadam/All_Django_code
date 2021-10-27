import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import Profile


def profile_upload(request):
    data = Profile.objects.all()
    if request.method == "GET":
        return render(request, 'profile_upload.html')
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = Profile.objects.update_or_create(
        name=column[0],
        email=column[1],
        address=column[2],
        phone=column[3],
        profile=column[4]
        )
    return render(request, 'profile_upload.html')
