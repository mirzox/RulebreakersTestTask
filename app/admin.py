from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'completed', 'created_at']


admin.site.register(Task, TaskAdmin)
