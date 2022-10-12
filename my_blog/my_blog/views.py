from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello !!, this is my first view in Django!!!")

def title(request):
    return HttpResponse("<h1>This is a Title in H1</h1>")