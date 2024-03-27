from django import forms

from back.models import UserModel, EventModel, AnotherUserModel


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'phone_number', 'faculty', 'group', 'event',)


class AnotherUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = AnotherUserModel
        fields = ('first_name', 'last_name', 'phone_number', 'academic_degree', 'event',)


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ('event_name', 'date', 'time',)
