from django.shortcuts import render
from django.http import HttpResponse

import csv
import os
from assignment.form import *
from assignment.models import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
#from as import forms
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate  , logout
from django.contrib import messages
import json


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
        	username = form.cleaned_data.get('username')
        	password = form.cleaned_data.get('password')
        	user = authenticate(username=username, password=password)
        	if user is not None:
        		login(request, user)
        		messages.info(request, f"You are now logged in as {username}.")
        		return redirect('list')
        	else:
        		messages.error(request,"Invalid username or password.")
    else:
    	form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})
    
    
def logout_user(request):
    logout(request)
    return redirect('login')
    


    
def form(request):
	frms = Studentform(request.POST or None ,request.FILES or None)
	if frms.is_valid():
		frms.save()
	return render(request,'add.html',{'form':frms})
	

def stu_update(request, id):  
    frms_obj = Student.objects.get(id=id)  
    form = Studentform(request.POST or None, request.FILES or None, instance = frms_obj)  
    if form.is_valid():  
        form.save() 
        #frms_obj=frms.objects.all()   
    return render(request, 'stu_update.html', {'form':form})
    
    

@login_required(redirect_field_name='list', login_url='login')
def list_view(request):
	frms_obj = Student.objects.all()
	return render(request,'list.html',{'form':frms_obj})   
	
	
def mark_view(request,id):
        dic = mark.objects.filter(stu_id=id).values()
        return render(request,'mark.html',{"data":dic})
   
def add(request):
    f = Markform(request.POST or None ,request.FILES or None)
    if f.is_valid():
        obj = f.save(commit=False)
        obj.created_by = (request.user).username
        #obj.modified_by = (request.user).username
        obj.save()
    return render(request,'mark_add.html',{'form':f})


def mark_update(request, id):  
    frms_obj = mark.objects.get(id=id)  
    form = Markform(request.POST or None, request.FILES or None, instance = frms_obj)  
    if form.is_valid(): 
        obj = form.save(commit=False)
        #obj.created_by = (request.user).username
        obj.modified_by = (request.user).username
        obj.save() 
        #frms_obj=frms.objects.all()   
    return render(request, 'mark_update.html', {'form':form})
    
def delete(request,id):
	frms_obj = mark.objects.get(id=id)
	frms_obj.delete()
	return render(request,'delete.html',{'form':frms_obj})
	
	
def dele(request,id):
	frms_obj = Student.objects.get(id=id)
	frms_obj.delete()
	return render(request,'studel.html',{'form':frms_obj})
	
#JSON DATA FORMAT

def json(request,id):
    import json
    l = []
    data = mark.objects.filter(id=id).values()
    print(data)
    for j in data:
        l.append(j)
    s = json.dumps(l, default=str, indent = 4)
    print(type(s))
    return HttpResponse(s, content_type="application/json")
   # return render(request,'json.html',{'json':s})



def con(request):
    import json
    l = []
    data = mark.objects.all().values()
    for j in data:
        l.append(j)
    s = json.dumps(l, default=str, indent = 4)
    return HttpResponse(s, content_type="application/json")
            
    
    
    


















	
	
	
