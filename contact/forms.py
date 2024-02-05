from django import forms
from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)
