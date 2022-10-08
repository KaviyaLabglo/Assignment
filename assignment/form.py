from urllib import request
from django import forms
from assignment.models import *




class Studentform(forms.ModelForm):
    class Meta:
    	model = Student
    	fields = "__all__" 
    	
class Markform(forms.ModelForm):
    class Meta:
    	model = mark
    	fields = ['stu_id', 'subject','mark']
    	

