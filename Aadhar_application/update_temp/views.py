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

def updateinfo(request):
	c = {}
	c.update(csrf(request))
	return render(request,'updateinfo.html',c)

def updatelist(request):
	c = {}
	c.update(csrf(request))
	number1=request.POST['number']
	uid=request.POST['anum']
	try:
		s1=newapp.objects.get(id=uid,number=number1)
		return render(request,'updatelist.html',c)
	except:
		messages.info(request,'invalid details please enter valid details')
		return render(request,'logedin.html',c)

def updatename(request):
	c = {}
	c.update(csrf(request))
	return render(request,'updatename.html',c)

def validname(request):
	messages.info(request,"name updated successfully...  thank you!!")
	c = {}
	c.update(csrf(request))
	return render(request,'updatelist.html',c)

def updateDOB(request):
	c = {}
	c.update(csrf(request))
	return render(request,'updateDOB.html',c)

def validDOB(request):
	messages.info(request,"Date of Birth updated successfully...  thank you!!")
	c = {}
	c.update(csrf(request))
	return render(request,'updatelist.html',c)

def updateadd(request):
	c = {}
	c.update(csrf(request))
	return render(request,'updateadd.html',c)

def validadd(request):
	messages.info(request,"Address updated successfully...  thank you!!")
	c = {}
	c.update(csrf(request))
	return render(request,'updatelist.html',c)

def updatephoto(request):
	c = {}
	c.update(csrf(request))
	return render(request,'updatephoto.html',c)

def validphoto(request):
	messages.info(request,"Photo updated successfully...  thank you!!")
	c = {}
	c.update(csrf(request))
	return render(request,'updatelist.html',c)