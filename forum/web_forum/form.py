from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from web_forum.models import Discussion
from django.contrib.auth.models import User


def validate_title(value):
    if len(value) < 4:
        raise ValidationError('Summary must be greater than four')


def validate_detailed_description(value):
    if 'N-word' in value:
        raise ValidationError('Description contains a bad word')


class UserForm(forms.Form):
    user_name = forms.CharField(max_length=50, required=True, label="Юзер")

    def clean_username(self):
        username = self.cleaned_data['username']
        user_exists = User.objects.filter(username=username).exists()


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class DiscussionForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True, label="Название")
    description = forms.CharField(max_length=200, required=True, label="Описание")

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)

        for v in self.visible_fields():
            if not isinstance(v.field.widget, widgets.CheckboxSelectMultiple):
                v.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Discussion
        fields = ["title", "description", "author", "created_at"]
