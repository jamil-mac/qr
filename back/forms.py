from django import forms

from back.models import UserModel, EventModel


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'phone_number', 'event',)


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ('event_name', 'date', 'time',)
