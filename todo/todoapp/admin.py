from django.contrib import admin
from todoapp.models import AllTasks

# Register your models here.
@admin.register(AllTasks)
class ModeladminAllTasks(admin.ModelAdmin):
    list_display=['Task_name','about_task','task_priority','created_at']

