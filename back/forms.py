from django import forms

from back.models import UserModel


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'phone_number', 'event')
