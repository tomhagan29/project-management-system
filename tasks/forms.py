from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["project", "title", "description"]

        widgets = {
            "project": forms.Select(attrs={"class": "form-select"}),
            "title": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "type": "text", "rows": 4}
            ),
        }


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "status", "description"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
            "status": forms.Select(
                attrs={"class": "form-select"}, choices=Task.status.field.choices
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "type": "text", "rows": 4}
            ),
        }
