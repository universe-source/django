from __future__ import unicode_literals

from django import forms
from django.db import models
from django.contrib.auth.models import User


class Person(User):
    class Meta:
        proxy = True


class LoginForm(forms.Form):
    # This creates two variables called username and password that are assigned form character fields
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
