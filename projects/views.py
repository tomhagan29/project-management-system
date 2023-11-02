from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ProjectForm
from .models import Project
from tasks.models import Task


# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "projects/index.html", {"projects": projects})


def create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            title = request.POST["title"]
            code = request.POST["code"]
            description = request.POST["description"]
            new_project = Project(title=title, code=code, description=description)
            new_project.save()
            return HttpResponseRedirect("/projects/")
    else:
        form = ProjectForm()

    return render(request, "projects/create.html", {"form": form})


def details(request, project_id):
    project_details = Project.objects.get(pk=project_id)
    todo_tasks = Task.objects.filter(project=project_id, status="TODO")
    in_progress_tasks = Task.objects.filter(project=project_id, status="In-Progress")
    review_tasks = Task.objects.filter(project=project_id, status="Review")
    completed_tasks = Task.objects.filter(project=project_id, status="Completed")
    return render(
        request,
        "projects/details.html",
        {
            "project": project_details,
            "todo_tasks": todo_tasks,
            "in_progress_tasks": in_progress_tasks,
            "review_tasks": review_tasks,
            "completed_tasks": completed_tasks,
        },
    )


def update(request, project_id):
    project = Project.objects.get(pk=project_id)

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project.title = request.POST["title"]
            project.code = request.POST["code"]
            project.description = request.POST["description"]
            project.save()
            return HttpResponseRedirect(f"/projects/{project_id}")
    else:
        form = ProjectForm(
            initial={
                "title": project.title,
                "code": project.code,
                "description": project.description,
            }
        )

    return render(request, "projects/update.html", {"form": form})


def delete(request, project_id):
    project = Project.objects.get(pk=project_id)
    project.delete()
    return HttpResponseRedirect("/projects")
