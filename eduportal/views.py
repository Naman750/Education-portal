from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse("<h1>Welcome  eduportal  page </h1>")
    return render(request,"eduportal/home.html")
def contact(request):
    return render(request,"eduportal/contact.html")
def about(request):
    return render(request,"eduportal/about.html")
def user(request):
    return render(request,"eduportal/user.html")



