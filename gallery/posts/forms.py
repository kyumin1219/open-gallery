from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Artist, Artwork


class SignUpForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '비밀번호를 입력해주세요.',
        'required': 'required'
    }))

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
            'email': forms.EmailInput(attrs={
                'placeholder': '이메일을 입력해주세요.',
                'required': 'required'
            }),
        }

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.password = make_password(self.cleaned_data['password'])  # 비밀번호 해싱
        if commit:
            user.save()
        return user

class ArtistRegistrationForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['profile_image', 'name', 'gender', 'birth_date', 'email', 'contact']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'contact': forms.TextInput(attrs={'placeholder': '000-0000-0000'}),
        }

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'price', 'hoosu', 'artwork_image']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('가격은 0 이상의 숫자여야 합니다.')
        return price

    def clean_hoosu(self):
        hoosu = self.cleaned_data.get('hoosu')
        if hoosu < 1 or hoosu > 500:
            raise forms.ValidationError('호수는 1에서 500 사이의 값이어야 합니다.')
        return hoosu