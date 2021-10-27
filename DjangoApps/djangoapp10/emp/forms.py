from emp.models import Employee
from django import forms
class EmpSignUpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'