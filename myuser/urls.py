"""eduportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path, include
from myuser import views
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path("",views.index, name= "userpage"),
    path("about",views.about, name= "about"),
    path("home",views.home, name= "home"),
    path("contact",views.contact, name= "contact"),
    path("services",views.services, name= "services"),
    path("showcourses",views.showcourses, name= "showcourses"),
    path("regcourse",views.regcourse, name= "regcourse"),
    path("userreg",views.userreg, name= "userreg"),
    path("showusers",views.showusers, name= "showusers"),
    path("showcourses",views.showcourses, name= "showcourses"),
    path("courseApply",views.courseApply, name= "courseApply"),
    path("showcourseApply",views.showcourseApply, name= "showcourseApply"),
    path("searchusers",views.searchusers, name= "searchusers"),
    path("loginform",views.loginform, name= "loginform"),
    path("usershowcourses",views.usershowcourses, name= "usershowcourses"),
    path("purchase",views.purchase, name= "purchase"),
    path("payment",views.payment, name= "payment"),
    path("searchcourses",views.searchcourses, name= "searchcourses"),
    path("userhomeafterlogin",views.userhomeafterlogin, name= "userhomeafterlogin"),
    path("usershowusers",views.usershowusers, name= "usershowusers"),
     
    
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
