from django.http import HttpResponse

# Create your views here.
def hi(request, parametro):
    return HttpResponse(f"<h1>Hola {parametro}</h1>")
    # return HttpResponse("<h1>Hola %s</h1>" % parametro)

def about(request):
    return HttpResponse("about")

def index(request):
    return HttpResponse("index")