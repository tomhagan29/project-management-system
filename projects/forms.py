from django import forms
from .models import Project

# class ProjectForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     code = forms.CharField(max_length=5)
#     description = forms.CharField(max_length=300)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "code", "description"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
            "code": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "type": "text", "rows": 4}
            ),
        }
