from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth ,messages
from django.contrib.auth.models import auth ,User
from django.template.context_processors import csrf
from new_Aadhar.models import newapp
from django.core import serializers
import random

# Create your views here.




def downloadinfo(request):
    c = {}
    c.update(csrf(request))
    return render(request,'downloadinfo.html',c)


def downloadvalid(request):
	c = {}
	c.update(csrf(request))
	number1=request.POST['number']
	uid=request.POST['anum']
	try:
		s1=newapp.objects.get(id=uid,number=number1)
		return render(request,'displayaadhar.html',{'test':s1})
	except:
		messages.info(request,'invalid details please enter valid details')
		return render(request,'logedin.html',c)
