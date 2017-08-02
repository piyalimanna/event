from django.contrib.auth.models import User
from django import forms
from .models import *

class TeamForm(forms.Form):
	name = forms.CharField(max_length=50,label='Name (Username):')
	password = forms.CharField(widget=forms.PasswordInput(),max_length=50)
	name = forms.CharField(max_length=50,label='Name of Participant :')
	phone = forms.IntegerField(widget=forms.TextInput(),min_value=6000000000,label='Phone of Participant :')
	email = forms.EmailField(label='Email of Participant :')

class LoginForm(forms.Form):
	name = forms.CharField(max_length = 50)
	password = forms.CharField(widget=forms.PasswordInput())

class QSForm(forms.Form):
	answer=forms.CharField(max_length=50)