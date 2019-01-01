from django import forms
from crypto.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('email', 'full_name', 'message')
