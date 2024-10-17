# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': '이름을 입력해주세요.',
                'required': 'required'
            }),
            'username': forms.TextInput(attrs={
                'placeholder': '아이디를 입력해주세요.',
                'required': 'required'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': '비밀번호를 입력해주세요.',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': '이메일을 입력해주세요.',
                'required': 'required'
            }),
        }
