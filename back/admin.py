from django.contrib import admin

from back.models import EventModel, UserModel, FacultyModel, GroupModel, AnotherUserModel


@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'date', 'time']


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'faculty', 'event']


@admin.register(AnotherUserModel)
class AnotherUserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'academic_degree', 'first_name', 'last_name']


@admin.register(FacultyModel)
class FacultyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'faculty_name', 'abbreviation']


@admin.register(GroupModel)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_name']
