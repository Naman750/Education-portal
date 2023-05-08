from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Welcome administaror page")

def about(request):
    return HttpResponse("Welcome user admin -> about")
def contact(request):
    return HttpResponse("Welcome user admin -> contact")
def  services(request):
    return HttpResponse("Welcome user admin -> services")
