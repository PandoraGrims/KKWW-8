from django.forms import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    email = forms.EmailField(required=True, label='Email')
    avatar_url = forms.URLField(required=True, label='Аватарка')

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not first_name and not last_name:
            raise forms.ValidationError('Введите хотя бы одно из полей "Имя" или "Фамилия".')

        return cleaned_data

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'last_name', 'avatar_url', 'email']
