from django.http import HttpResponse

# Create your views here.
def hi(request):
    return HttpResponse("<h1>Hola buenas</h1>")

def about(request):
    return HttpResponse("about")