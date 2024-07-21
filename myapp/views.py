from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def hi(request, parametro):
    return HttpResponse(f"<h1>Hola {parametro}</h1>")
    # return HttpResponse("<h1>Hola %s</h1>" % parametro)

def index(request):
    data = {
        "title": "Titulo de la pagina"
    }

    return render(request, "index.html", data)

def about(request):
    data = {
        "username": "Hyromy"
    }

    return render(request, "about.html", data)

def projects(request):
    projects = Project.objects.all()

    data = {
        "projects": projects
    }

    return render(request, "projects.html", data)

def tasks(request, id):
    task = get_object_or_404(Task, id = id)
    return HttpResponse(f"task: {task.title}")