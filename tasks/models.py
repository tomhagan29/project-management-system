from django.db import models
from projects.models import Project

status_choices = [
    ("todo", "Todo"),
    ("in-progress", "In-Progress"),
    ("review", "Review"),
    ("completed", "Completed"),
]


# Create your models here.
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reference = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=15, choices=status_choices, default="TODO")
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.reference)
