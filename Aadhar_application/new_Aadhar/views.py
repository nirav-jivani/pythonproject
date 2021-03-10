from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth ,messages
from django.contrib.auth.models import auth ,User
from django.template.context_processors import csrf
from new_Aadhar.models import newapp
from django.core import serializers
from .forms import imageupload
import random
from datetime import date
import calendar
import time 
# Create your views here.

def address(request):
	c = {}
	c.update(csrf(request))
	return render(request,'new_aadhar.html', c)
	
def dob(request):
	c = {}
	c.update(csrf(request))
	request.session['address']=(request.POST['house'] + "- " + request.POST['area'] +" " + request.POST['tv'] + " " + request.POST['dist']
						   +" " +request.POST['state'] +" "+request.POST['pincode'])
	temp=request.session['rdate']=request.POST['date']
	if(temp>str(date.today())):
		messages.info(request,"date is invalid ....")
		return render(request,'new_aadhar.html', c)
	return render(request,'dob.html', c)

def personal(request):
	request.session['baddress']=(request.POST['tv'] + " " + request.POST['dist']+" " +request.POST['state'] +" "+request.POST['pincode'])
	temp=request.session['bdate']=request.POST['date']
	c = {}
	c.update(csrf(request))
	if(temp>str(date.today())):
		messages.info(request,"date is invalid ....")
		return render(request,'dob.html', c)
	return render(request,'personal.html', c)
	
def declaration(request):
	request.session['name']=(request.POST['name']+" "+request.POST['surname'])
	request.session['gender']=request.POST['gender']
	request.session['relation']=request.POST['relation']
	request.session['rname']=(request.POST['rname']+" "+request.POST['rsurname'])
	c = {}
	c.update(csrf(request))
	return render(request,'dec.html', c)

def proof(request):
	request.session['number1']=request.POST['number1']
	request.session['email']=request.POST['email']
	request.session['place']=request.POST['place']
	temp=request.session['fdate']=request.POST['date']
	c = {}
	c.update(csrf(request))
	if(temp>str(date.today())):
		messages.info(request,"date is invalid ....")
		return render(request,'dec.html', c)
	test={}
	test['form']=imageupload();
	return render(request,'proof.html',test)

def preview(request):
	uidt=random.randint(10000000000,99999999999)
	ts = calendar.timegm(time.gmtime())
	uidt=(str(uidt)+str(ts))
	request.session['uid']=uidt
	c = {}
	c.update(csrf(request))
	request.session['addfname']=request.POST['adp']
	request.session['agefname']=request.POST['agep']
	test=imageupload(request.POST,request.FILES)
	ls=newapp(name=request.session['name'],gender=request.session['gender']
	,address=request.session['address']
	,relationtype=request.session['relation']
	,relativename=request.session['rname']
	,birthaddress=request.session['baddress']
	,birthdate=request.session['bdate']
	,number=request.session['number1']
	,email=request.session['email']
	,rdate=request.session['rdate']
	,fdate=request.session['fdate']
	,place=request.session['place']
	,addfname=request.session['addfname']
	,agefname=request.session['agefname']
	,addf=request.FILES['file1']
	,agef=request.FILES['file2']
	,phf=request.FILES['file3']
	,vid=uidt);
	try:
		temp=newapp.object.get(birthdate=request.session['bdate'],name=request.session['name'])
		messages.info(request,"user already exist your Aadhar already made please visit nearest branch")
		return render(request,'logedin.html',c)
	except:
		ls.save();
		return render(request,'details.html',{'it':ls})

def submitform(request):
	c = {}
	c.update(csrf(request))
	messages.info(request,"your registeration sucessfully....  your vid/aadhar card number is "+str(request.session['uid']) +' pelase first get your Aadhar number from genaration section using vid')
	return render(request,'logedin.html',c)