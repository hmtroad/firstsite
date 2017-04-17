# --- created by myself
#----coding: utf-8--------
from django import forms
# class AddForm(forms.Form):

class LoginForm(forms.Form):
    user = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())
    # DateInput, CheckboxInput and so on.
    def clean_message(self):
        if self.user:
            return self.user
