from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def hi(request, parametro):
    return HttpResponse(f"<h1>Hola {parametro}</h1>")
    # return HttpResponse("<h1>Hola %s</h1>" % parametro)

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe = False)

def tasks(request, id):
    task = get_object_or_404(Task, id = id)
    return HttpResponse(f"task: {task.title}")