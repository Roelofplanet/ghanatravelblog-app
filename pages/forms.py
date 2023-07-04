from django import forms
from django.forms import TextInput, EmailInput


class ContactForm(forms.Form):
    from_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"style": "width: 600px;", "class": "form-control"}
        ),
    )
    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"style": "width: 600px;", "class": "form-control"}
        ),
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"style": "width: 600px;", "class": "form-control"}
        ),
    )
