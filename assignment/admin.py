from django.contrib import admin
from assignment.models import *

class S(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','dob','age','upload_image')
admin.site.register(Student,S)
      
class M(admin.ModelAdmin):
    list_display = ('stu_id','subject', 'mark', 'updated_on', 'created_on')
admin.site.register(mark,M)
