from django.db import models
from django.contrib.auth.models import User

class userReg(models.Model):
    uid =  models.IntegerField()
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mobile = models.IntegerField()
    uimg = models.ImageField(upload_to= "uimg/",  max_length= 100 , null= True)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    dob = models.DateField(null=True, blank=True)
    repw = models.CharField(max_length=30)
    


class CourseReg(models.Model):
    uid =  models.IntegerField()
    cname = models.TextField()
    startdate = models.DateField()
    cbatch =  models.CharField(max_length=30)
    batchday = models.CharField(max_length=30)
    cimg = models.ImageField(upload_to= "cimg/",  max_length= 100)
    cprice = models.IntegerField()
    

class CourseReg1(models.Model):
    cname = models.CharField(max_length=30)
    csyll = models.CharField(max_length=100)
    cfee = models.IntegerField()
    cdur = models.CharField(max_length=30) 

class CourseApply(models.Model):
    cname = models.CharField(max_length=30)
    startdate = models.CharField(max_length=30)
    cbatch = models.CharField(max_length=30) 
    batchday = models.CharField(max_length=30) 



    
    

 