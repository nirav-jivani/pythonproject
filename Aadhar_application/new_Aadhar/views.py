from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth ,messages
from django.contrib.auth.models import auth ,User
from django.template.context_processors import csrf
from new_Aadhar.models import newapp
from django.core import serializers
import base64
# Create your views here.

def address(request):
	c = {}
	c.update(csrf(request))
	return render(request,'new_aadhar.html', c)
	
def dob(request):
	request.session['address']=(request.POST['house'] + "- " + request.POST['area'] +" " + request.POST['tv'] + " " + request.POST['dist']
						   +" " +request.POST['state'] +" "+request.POST['pincode'])
	request.session['rdate']=request.POST['date']
	c = {}
	c.update(csrf(request))
	return render(request,'dob.html', c)

def personal(request):
	request.session['baddress']=(request.POST['tv'] + " " + request.POST['dist']+" " +request.POST['state'] +" "+request.POST['pincode'])
	request.session['bdate']=request.POST['date']
	c = {}
	c.update(csrf(request))
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
	request.session['fdate']=request.POST['date']
	c = {}
	c.update(csrf(request))
	return render(request,'proof.html', c)

def preview(request):
	c = {}
	c.update(csrf(request))
	request.session['addfname']=request.POST['adp']
	request.session['agefname']=request.POST['agep']
	request.session['addf']=request.POST.getlist('addfile')
	request.session['agef']=request.POST.getlist('agefile')
	temp=request.session['phf']=request.POST.getlist('phfile')
	ls=newapp(c,name=request.session['name'],gender=request.session['gender']
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
	,phf=temp[0]);
	
	return render(request,'details.html',{'it':ls})

def submitform(request):
	addf1=request.session['addf']
	agef1=request.session['agef']
	phf1=request.session['phf']
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
	,addf=addf1[0]
	,agef=agef1[0]
	,phf=phf1[0]);
	ls.save();
	c = {}
	c.update(csrf(request))
	messages.info(request,"your registeration sucessfully..../n  your uid/aadhar card number is ")
	return render(request,'logedin.html',c)