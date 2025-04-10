from django.db import models

# Create your models here.

class AllTasks(models.Model):
    Task_name = models.CharField(max_length=100)
    about_task=models.CharField(max_length=250)
    task_priority=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Task_name
