from modeltranslation.translator import TranslationOptions, register

from back.models import EventModel, FacultyModel


@register(EventModel)
class EventTranslationOptions(TranslationOptions):
    fields = ('event_name',)


@register(FacultyModel)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('faculty_name', 'abbreviation',)
