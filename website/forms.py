from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(validators=[EmailValidator()])
    subject =forms.CharField(max_length=200, widget=forms.Textarea(attrs={"class":"form-control"}))
    message = forms.CharField(max_length=200, widget=forms.Textarea(attrs={"class":"form-control"}))
