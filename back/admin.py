from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin

from back.models import EventModel, UserModel, FacultyModel, GroupModel


class MyTranslationAdmin(TabbedTranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(EventModel)
class EventModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'event_name', 'date', 'time']


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'faculty', 'event']


@admin.register(FacultyModel)
class FacultyModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'faculty_name', 'abbreviation']


@admin.register(GroupModel)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_name']
