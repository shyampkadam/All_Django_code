
from django import forms
from mycrudapp.models import Students
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"