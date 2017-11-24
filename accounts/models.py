"""
Account models
"""
from django import forms
#  from django.db import models
from django.contrib.auth.models import User


class Accounts(User):
    class Meta:
        proxy = True


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
