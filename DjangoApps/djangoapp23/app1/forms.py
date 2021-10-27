from django import forms


class SubscribeForm(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email
