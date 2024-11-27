from django import forms
class UserRegistr(forms.Form):
    username = forms.CharField(max_length=30, label= 'Введите логин:')
    password = forms.CharField(min_length=8, label='Введите пароль:')
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль:')
    age = forms.IntegerField(min_value=18,max_value=103, label="Введите свой возраст:")