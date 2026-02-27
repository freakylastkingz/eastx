from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    
