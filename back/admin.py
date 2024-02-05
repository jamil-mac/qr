from django.contrib import admin

from back.models import EventModel, UserModel, FacultyModel, GroupModel

# admin.site.register(UserModel)
admin.site.register(FacultyModel)
admin.site.register(GroupModel)


@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'date', 'time']


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'faculty', 'event']
