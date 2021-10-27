from django import forms

class Form1(forms.Form):
    name=forms.CharField()

class Form2(forms.Form):
    city=forms.CharField()

class Form3(forms.Form):
    age=forms.IntegerField()