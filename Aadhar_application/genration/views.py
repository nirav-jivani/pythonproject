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
    s1=newapp.objects.get(number=number1,vid=vid)
    temp=s1.id
    return render(request,'displaynumber.html',{'nm':temp})
	
def genremaster(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		num=request.POST['number']
		if newapp.objects.filter(number=num): 
			request.session['number']=num
			return redirect('/send2')
		else:
			messages.info(request,"user can not found please register...")
			return render(request,'genre.html',c)
	return render(request,'genremaster.html',c)
	
def send2(request):
	num=request.session['number']
	num1="+91"+str(num)
	id='ACed978f63efe65f095d94a2785e2c2555'
	token='4c7bb688f9dfb853d04f466de101a8ab'
	client=Client(id,token)
	otp=random.randint(1000,9999)
	request.session['otps2']=otp;
	client.messages.create(
	body="your otp for for verfication is "+str(otp),
	from_='+16789522224',
	to=num1
	)
	c = {}
	c.update(csrf(request))
	messages.info(request,"master otp send successfully.....")
	return render(request,'logedin.html', c)