from django.db import models

class userReg3(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mobile = models.IntegerField()
    dob = models.DateField()

# Create your models here.
