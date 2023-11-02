from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="project_index"),
    path("create", views.create, name="project_create"),
    path("<int:project_id>", views.details, name="project_details"),
    path("<int:project_id>/update", views.update, name="project_update"),
    path("<int:project_id>/delete", views.delete, name="project_delete"),
]
