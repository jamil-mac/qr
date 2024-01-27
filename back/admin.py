from django.contrib import admin

from back.models import EventModel, UserModel, FacultyModel, GroupModel

admin.site.register(EventModel)
admin.site.register(UserModel)
admin.site.register(FacultyModel)
admin.site.register(GroupModel)
