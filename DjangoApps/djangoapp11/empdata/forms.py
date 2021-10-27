from django import forms
from django.core import validators

def is_first_letter_capital(value):
    if value.istitle() !=  True:
        raise forms.ValidationError('First Letter should be capital')

class EmpSignInForm(forms.Form):
    fullName=forms.CharField(max_length=10, help_text='10 characters max.')
    age=forms.IntegerField()
    # Approach2: Using inbuilt validators
    city=forms.CharField(validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(10)])
    email=forms.EmailField()
    # Approach3: Using custom validators
    password=forms.CharField(widget=forms.PasswordInput(),validators=[is_first_letter_capital])
    address=forms.CharField(widget=forms.Textarea)
    # Approach1: Using clean_fieldname()
    def clean_fullName(self):
        print('Validating fullName')
        fn=self.cleaned_data['fullName']
        if len(fn)<5:
            raise forms.ValidationError('Your name must be greater than 5 letters')
        return fn
    def clean_age(self):
        print('Validating age')
        age = self.cleaned_data['age']
        if age > 100:
            raise forms.ValidationError('Age must be less than 100')
        return age


