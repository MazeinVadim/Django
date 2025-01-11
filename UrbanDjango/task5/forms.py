from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="Введите логин",
        widget=forms.TextInput(attrs={'required': True})
    )
    password = forms.CharField(
        min_length=8,
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={'required': True})
    )
    repeat_password = forms.CharField(
        min_length=8,
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'required': True})
    )
    age = forms.CharField(
        max_length=3,
        label="Введите свой возраст",
        widget=forms.TextInput(attrs={'required': True})
    )