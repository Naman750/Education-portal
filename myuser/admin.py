from django.contrib import admin
from myuser.models import userReg
from myuser.models import CourseReg
from myuser.models import CourseReg1
from myuser.models import CourseApply
from myuser.models import QuizQuestion
from myuser.models import adminuser
from myuser.models import Attendance




# Register your models here.
admin.site.register(userReg)
admin.site.register(CourseReg)
admin.site.register(CourseReg1)
admin.site.register(CourseApply)
admin.site.register(QuizQuestion)
admin.site.register(adminuser)
admin.site.register(Attendance)


