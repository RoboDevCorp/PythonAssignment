from django import forms
from .models import UrlDetails

class RegisterUrlForm(forms.ModelForm):
    class Meta:
        model = UrlDetails
        fields = ['long_url']
