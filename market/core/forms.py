from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2') 

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your username",
                "class": "w-full py-4 px-6 rounded-xl"
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email",
                "class": "w-full py-4 px-6 rounded-xl"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your password",
                "class": "w-full py-4 px-6 rounded-xl"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your password",
                "class": "w-full py-4 px-6 rounded-xl"
            }
        )
    )