from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import TaskForm, TaskEditForm
from .models import Task
from projects.models import Project


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {"tasks": tasks})


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            project = Project.objects.get(pk=request.POST["project"])
            project_ref = f"{project.code}-{project.ticket_count + 1}"
            title = request.POST["title"]
            description = request.POST["description"]
            new_task = Task(
                project=project,
                reference=project_ref,
                title=title,
                description=description,
            )
            new_task.save()
            project.ticket_count += 1
            project.save()
            return HttpResponseRedirect(f"/projects/{project.id}")
    else:
        form = TaskForm()
        projects = Project.objects.all()

    return render(request, "tasks/create.html", {"projects": projects, "form": form})


def details(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, "tasks/details.html", {"task": task})


def update(request, task_id):
    # Add input validation
    task = Task.objects.get(pk=task_id)

    if request.method == "POST":
        form = TaskEditForm(request)
        if form.is_valid():
            task.title = request.POST["title"]
            task.status = request.POST["status"]
            task.description = request.POST["description"]
            task.save()
            return HttpResponseRedirect(f"/tasks/")
    else:
        form = TaskEditForm(
            initial={
                "title": task.title,
                "status": task.status,
                "description": task.description,
            }
        )

    return render(request, "tasks/update.html", {"form": form, "task": task})

    # if request.method == "POST":
    #     task = Task.objects.get(pk=task_id)
    #     task.title = request.POST["title"]
    #     task.status = request.POST["status"]
    #     task.description = request.POST["description"]
    #     task.save()
    #     return HttpResponseRedirect(f"/tasks/")
    # else:
    #     task = Task.objects.get(pk=task_id)
    #     statuses = [choice[1] for choice in Task.status.field.choices]
    #     return render(
    #         request, "tasks/update.html", {"task": task, "statuses": statuses}
    #     )


def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    project_id = task.project.id
    task.delete()
    return HttpResponseRedirect(f"/projects/{project_id}")
