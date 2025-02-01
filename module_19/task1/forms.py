from django import forms


class UserRegister(forms.Form):
    name = forms.CharField(max_length=20, required=True, label='Введите логин:')
    password = forms.CharField(required=True, label='Введите пароль:')
    repeat_password = forms.CharField(required=True, label='Повторите пароль:')
    age = forms.IntegerField(required=True, label='Введите свой возраст:')
