from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # fields = '__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title',  'another_title', 'authors', 'bibliographic_entry', 'abstract', 'abstract_in_another_language', 'URL', 'file', 'is_published', 'category', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'another_title': forms.TextInput(attrs={'class': 'form-control'}),
            'bibliographic_entry': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'abstract': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'abstract_in_another_language': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'URL': forms.URLInput(attrs={'class': 'form-control'}),
            'authors': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title