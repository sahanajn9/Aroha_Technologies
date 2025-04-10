from django import forms
from todoapp.models import AllTasks

class TaskForm(forms.ModelForm):
    class Meta:
        model=AllTasks
        fields="__all__"


class EditForm(forms.ModelForm):
    class Meta:
        model=AllTasks
        fields="__all__"