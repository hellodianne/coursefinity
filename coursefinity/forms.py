from django import forms
from django.contrib.auth.models import User
from coursefinity.models import UserProfile

class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="username.")
	email = forms.CharField(help_text="email")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="password")

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
