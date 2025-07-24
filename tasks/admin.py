from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'deadline_days', 'created_at']
    list_filter = ['priority', 'deadline_days']
    search_fields = ['title', 'description']
    ordering = ['deadline_days', '-priority']
