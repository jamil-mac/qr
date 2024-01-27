from django.contrib import admin

from back.models import EventModel, UserModel, FacultyModel, GroupModel

admin.site.register(EventModel)
# admin.site.register(UserModel)
admin.site.register(FacultyModel)
admin.site.register(GroupModel)


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'faculty', 'event']
