from django.shortcuts import render , redirect
#from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth ,messages
from django.contrib.auth.models import auth ,User
from django.template.context_processors import csrf
import twilio
from twilio.rest import Client
import random
from new_Aadhar.models import newapp

# Create your views here.

def genre(request):
    c = {}
    c.update(csrf(request))
    return render(request,'genre.html',c)

def genreadhar(request):
    c = {}
    c.update(csrf(request))
    return render(request,'genreadhar.html',c)

def displaynumber(request):
    vid=request.POST['vid']
    number1=request.POST['number']
    s1=newapp.objects.get(number=number1,uid=vid)
    temp=s1.id
    return render(request,'displaynumber.html',{'nm':temp})