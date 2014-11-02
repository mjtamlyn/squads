import copy

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import TrainingCategory, TrainingType, SessionLog, SessionSection, Score, Squad, User


class UserAdmin(BaseUserAdmin):
    fieldsets = copy.copy(BaseUserAdmin.fieldsets)
    fieldsets[0][1]['fields'] += ('squad', 'public_profile')


admin.site.register(TrainingCategory)
admin.site.register(TrainingType)
admin.site.register(SessionLog)
admin.site.register(SessionSection)
admin.site.register(Score)
admin.site.register(Squad)
admin.site.register(User, UserAdmin)
