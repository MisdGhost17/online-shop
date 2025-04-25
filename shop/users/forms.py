from users.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'login-form-username',
        'placeholder':'Введите логин',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'login-form-password',
        'placeholder':'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'last_name', 'first_name')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'register-form-username',
        'placeholder': 'Введите логин',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'register-form-password',
        'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'register-form-password',
        'placeholder': 'Введите пароль'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'register-form-email',
        'placeholder': 'Введите почту'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'register-form-name',
        'placeholder':'Введите Имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'register-form-name',
        'placeholder': 'Введите Фамилию'
    }))

class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'first_name', 'image',)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'change-form-username',
        'readonly': True,
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'change-form-email',
        'placeholder': 'Изменить email',
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'change-form-first_name',
        'placeholder': 'Изменить Имя',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'change-form-last_name',
        'placeholder': 'Изменить Фамилию',
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'change-image-form',
    }))
