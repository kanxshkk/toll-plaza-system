# main/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'car_number', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CreditForm(forms.Form):
    amount = forms.DecimalField()


class TollFeeForm(forms.Form):
    car_number = forms.CharField(label='Car Number')
    toll_fee = forms.DecimalField(label='Toll Fee')