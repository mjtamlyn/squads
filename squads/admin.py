from django.contrib import admin

from .models import TrainingCategory, TrainingType, SessionLog, SessionSection, Score


admin.site.register(TrainingCategory)
admin.site.register(TrainingType)
admin.site.register(SessionLog)
admin.site.register(SessionSection)
admin.site.register(Score)
