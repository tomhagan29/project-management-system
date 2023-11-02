from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=300)
    date_added = models.DateField(auto_now_add=True)
    ticket_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
