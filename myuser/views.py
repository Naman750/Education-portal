from django.shortcuts import render , HttpResponse
from  myuser.models import CourseReg
from  myuser.models import CourseReg1
from  myuser.models import CourseApply
from  myuser.models import adminuser
from  myuser.models import userReg
from  myuser.models import Attendance
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
from django.http import HttpResponse
from .forms import QuizForm
from .models import QuizQuestion



    
    
    

# Create your views here.

# Create your views here.
def quiz(request):
    try:    
      allquestion = QuizQuestion.objects.all()
      data = {"questions": allquestion}
      return render(request, 'myuser/quiz.html', data)
    except:
         return render(request, 'myuser/quiz.html')


def showattendance(request):
    try:   
        attendance = Attendance.objects.all()
        data = {"attendances": attendance }
        return render(request, 'myuser/showattendance.html', data)
    except:
         return render(request, 'myuser/showattendance.html')


def javaresult(request):
    try:
      allquestion = QuizQuestion.objects.all()
      data = {"questions": allquestion}   
      return render(request, 'myuser/javaresult.html',data )
    except:
         return render(request, 'myuser/javaresult.html')
    
def pythonresult(request):
    try:
      allquestion = QuizQuestion.objects.all()
      data = {"questions": allquestion}   
      return render(request, 'myuser/pythonresult.html',data )
    except:
         return render(request, 'myuser/pythonresult.html')
    
def phpresult(request):
    try:
      allquestion = QuizQuestion.objects.all()
      data = {"questions": allquestion}   
      return render(request, 'myuser/phpresult.html',data )
    except:
         return render(request, 'myuser/phpresult.html')
    
def nodejsresult(request):
    try:
      allquestion = QuizQuestion.objects.all()
      data = {"questions": allquestion}   
      return render(request, 'myuser/nodejsresult.html',data )
    except:
         return render(request, 'myuser/nodejsresult.html')
     




def index(request):
    #return HttpResponse("Welcome user page")
    #return render(request, "myuser/about.html")
    return render(request, "myuser/index.html")

def userlogout(request):
    #return HttpResponse("Welcome user page")
    #return render(request, "myuser/about.html")
    return render(request, "myuser/userlogout.html")

def userattendance(request):
          try:    
            uname = request.POST.get('name') # these fields are come from my user templates
            udate = request.POST.get('date')  # these fields are come from my user templates
            present_absent = request.POST.get('pora') 
            print(uname, udate , present_absent)
            result = Attendance(student_name = uname, date= udate,  present_absent = present_absent)
            result.save()
            print("Record Inserted for Userattendance ")
            return render(request, "myuser/userattendance.html")
          except:
               return render(request, "myuser/userattendance.html")
               
         
    
    



def userlogin(request):
                    try:                
                       lid = request.POST.get('lid')
                       pwd = request.POST.get('pwd') 
                       users = userReg.objects.filter(email = lid, password = pwd)
                       if len(users) == 0:
                            print("user is unauthenticated")
                            return render(request, "myuser/userlogout.html")
                       else:
                         print("user is authenticated")                                         
                         return render(request, "myuser/userlogin.html")
                    except:
                         
                         return render(request, "myuser/userlogout.html")
                                        
                        
    #return HttpResponse("Welcome user page")
    #return render(request, "myuser/about.html")
    






    
     
    
    #return HttpResponse("Welcome user page")
    #return render(request, "myuser/about.html")
    

def home(request):
    #return HttpResponse("Welcome user page")
    #return render(request, "myuser/about.html")
    return render(request, "myuser/home.html")

def about(request):
    #return HttpResponse("Welcome user  page -> about")
    return render(request, "myuser/about.html")

def userhomeafterlogin(request):
    #return HttpResponse("Welcome user  page -> about")
    return render(request, "myuser/userhomeafterlogin.html")





def adminlogout(request):
     return render(request, "myuser/adminlogout.html")

def payment(request):
     return render(request, "myuser/payment.html")


def purchase(request):
     if request.method == 'POST':
        # Get the credit card information from the form data
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        print(card_number,expiry_date,cvv)

        # Process the payment using a mock payment processor
        # Replace this with your actual payment processing logic
        if card_number and expiry_date and cvv:
            # Payment success
            return render(request,'myuser/payment.html')
        else:
            # Payment failed
            error = 'Invalid card information'
            return render(request, 'myuser/purchase.html', {'error': error})

     return render(request, 'myuser/purchase.html')

     
    

     



     
     
                    
    #return HttpResponse("Welcome user  page -> about")
    

def adminlogin(request):
                    try:                
                       lid = request.POST.get('lid')
                       pwd = request.POST.get('pwd') 
                       admin = adminuser.objects.filter(adminemail = lid, adminpassword = pwd)
                       if len(admin) == 0:
                            print("admin  is unauthenticated")
                            return render(request, "myuser/adminlogout.html")
                       else:
                         print("admin  is authenticated")                                         
                         return render(request, "myuser/adminlogin.html")
                    except:
                         
                         return render(request, "myuser/adminlogout.html")
             

        
    #return HttpResponse("Welcome user page -> contact")
def  services(request):
    #return HttpResponse("Welcome user page -> services")
    return render(request, "myuser/services.html")




def  regcourse(request):
    try:

        #print(request.POST != "POST")
        uidw = request.POST.get('uids')
        cname1 = request.POST.get('cname')
        startdate1 = request.POST.get('startdate')
        cbatch1 = request.POST.get('cbatch')
        batchday1  = request.POST.get('batchday')
        cprice1  = request.POST.get('cprice')  
        cimg1  = request.POST.get('image')  
        print(cname1,startdate1,cbatch1,batchday1,uidw,cprice1,cimg1)
        #res= CourseReg (cname= cname1, startdate= startdate1,cbatch =  cbatch1,batchday= batchday1)
        res= CourseReg (cname= cname1, startdate= startdate1,cbatch =  cbatch1,batchday= batchday1,uid = uidw,cprice =cprice1, cimg= cimg1  )
       # res= CourseReg1 (cname= cname1, startdate= startdate1,cbatch =  cbatch1,batchday= batchday1)
        res.save()
        #print("Record Inserted for courseReg")
        print("Record Inserted for courseReg")

    #return HttpResponse("Welcome user page -> regcourse")
        return render(request, "myuser/regcourse.html")
    except:
       return render(request, "myuser/regcourse.html")
    
def userreg(request):
    try:
        #print(request.POST != "POST")
        uidw = request.POST.get('uids')
        fname1 = request.POST.get('fname') # these fields are come from my user templates
        lname1 = request.POST.get('lname')  # these fields are come from my user templates
        dob1 = request.POST.get('dob')  # these fields are come from my user templates
        umob1  = request.POST.get('umob')  # these fields are come from my user templates
        email1  = request.POST.get('email')  # these fields are come from my user templates
        pwd1  = request.POST.get('pwd')  # these fields are come from my user templates
        rpwd1  = request.POST.get('rpwd')  # these fields are come from my user templates
        cimg1  = request.POST.get('image')
        if (pwd1 == rpwd1):
            print(fname1,lname1,dob1,umob1,email1,pwd1,uidw,cimg1)
            res =  userReg (fname= fname1, lname= lname1, mobile = umob1, email = email1, password = pwd1,dob = dob1,repw = rpwd1,uid = uidw, uimg = cimg1)
            # These fields are come from myuser models
            res.save()
            print("Record Inserted for UserReg ")
        else:
            print("password and Repassword not match")
        return render(request, "myuser/userreg.html")
    except:
        return render(request, "myuser/userreg.html")

def  courseApply(request):
    try:

        #print(request.POST != "POST")
        cname1 = request.POST.get('cname')
        startdate1 = request.POST.get('startdate')
        cbatch1 = request.POST.get('cbatch')
        batchday1  = request.POST.get('batchday')
        print(cname1,startdate1,cbatch1,batchday1)
        #res= CourseReg (cname= cname1, startdate= startdate1,cbatch =  cbatch1,batchday= batchday1)
        res=   CourseApply (cname= cname1, startdate= startdate1,cbatch =  cbatch1,batchday= batchday1)
       # res= CourseReg1 (cname= cname1, startdate= startdate1,cbatch =  cbatch1,batchday= batchday1)
        res.save()
        #print("Record Inserted for courseReg")
        print("Record Inserted for courseApply")

    #return HttpResponse("Welcome user page -> regcourse")
        return render(request, "myuser/courseApply.html")
    except:
       return render(request, "myuser/courseApply.html")

def showusers(request):
    try:
         allusers = userReg.objects.all()
         print("show all users: ",allusers)
         data = {"users":allusers}
         return render(request, "myuser/showusers.html",data)
    except:
         return render(request, "myuser/showusers.html")
    
     
    
def showcourses(request):
    try:
            allcourses = CourseReg.objects.all()
            print("show all courses",allcourses)
            data = {"key1":"value1","key2": "value2","courses": allcourses}
            return render(request, "myuser/showcourses.html",data)
    except:
        return render(request, "myuser/showcourses.html")
    
def usershowcourses(request):
    try:
            allcourses = CourseReg.objects.all()
            print("show all courses",allcourses)
            data = {"key1":"value1","key2": "value2","courses": allcourses}
            return render(request, "myuser/usershowcourses.html",data)
    except:
        return render(request, "myuser/usershowcourses.html")

def usershowusers(request):
    try:
            allusers = userReg.objects.all()
            print("show all courses",allusers)
            data = {"key1":"value1","key2": "value2","users": allusers}
            return render(request, "myuser/usershowusers.html",data)
    except:
        return render(request, "myuser/usershowusers.html")
    
    
def showcourseApply(request):
    try:
            allcourseApply = CourseApply.objects.all()
            print("show all course Apply",allcourseApply)
            data = {"key1":"value1","key2": "value2","showcoursesApply": allcourseApply}
            return render(request, "myuser/showcourseApply.html",data)
    except:
        return render(request, "myuser/showcourseApply.html")
    
    
def searchusers(request):
    try:
            sname = request.POST.get('fname') 
            print("test1",sname)
            print("test2",len(sname))
            if len(sname) > 0:
                 searchedusers = userReg.objects.filter(fname = sname) # to be dynamic
            else:
                 searchedusers = userReg.objects.all()
                 
            print("show searched users",searchedusers)
            data = {"susers": searchedusers}
            print("Data is searched")
            
                 
            return render(request, "myuser/searchusers.html",data)
    except:
        return render(request, "myuser/searchusers.html")
    
def searchcourses(request):
    try:
            sname = request.POST.get('cname') 
            print("test1",sname)
            print("test2",len(sname))
            if len(sname) > 0:
                 searchedusers = CourseReg.objects.filter(cname = sname) # to be dynamic
            else:
                 searchedusers = CourseReg.objects.all()
                 
            print("show searched users",searchedusers)
            data = {"scourses": searchedusers}
            print("Data is searched")
            
                 
            return render(request, "myuser/searchcourses.html",data)
    except:
        return render(request, "myuser/searchcourses.html")
       



