from django import forms
from django.core import validators

def check_name(value):
    if value[0].lower() == '$':
        raise forms.ValidationError("Name cannot start with $")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_name])
    email = forms.EmailField()
    verifyEmail = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)


    def clean(self):
        all_cleaned_data = super().clean()

        email = all_cleaned_data['email']
        verify_email = all_cleaned_data['verifyEmail']

        if email != verify_email:
            raise forms.ValidationError("EMAIL-IDS dont match")