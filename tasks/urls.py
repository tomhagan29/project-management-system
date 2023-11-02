from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="task_index"),
    path("create", views.create, name="task_create"),
    path("<int:task_id>", views.details, name="task_details"),
    path("<int:task_id>/update", views.update, name="task_update"),
    path("<int:task_id>/delete", views.delete, name="task_delete"),
]
