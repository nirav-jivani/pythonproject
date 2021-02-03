from django.shortcuts import render
#from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
import twilio
from twilio.rest import Client
import random
# Create your views here.


def index(request):
	return render(request,'index.html');
	
def register(request):
	c = {}
	c.update(csrf(request))
	return render(request,'signup.html', c)

def verify(request):
	num=request.POST.get('number','')
	if 'nums' not in request.session:
		request.session['nums']=num;
	num=request.session['nums'];
	num1="+91"+str(num)
	id='ACcb7ef5f8344eb9e6286fdb69703a2e3c'
	token='50664c92a29aaadcb6076273c415e22b'
	client=Client(id,token)
	otp=random.randint(1000,9999)
	request.session['otps']=otp;
	client.messages.create(
	body="your otp for for verfication is "+str(otp),
	from_='+17084017359',
	to=num1
	)
	c = {}
	c.update(csrf(request))
	return render(request,'verification.html', c)
	
def check(request):
	user=request.POST.get('user','')
	password=request.POST.get('pass','')
	us=auth.authenticate(username=user,password=password);
	
	if us is not None:
		auth.login(request,us)
		return HttpResponseRedirect('logedin')
	else:
		return HttpResponseRedirect('invalid')
		
def logedin(request):
	c = {}
	c.update(csrf(request))
	return render(request,'logedin.html', c)

def invalid(request):
	c = {}
	c.update(csrf(request))
	return render(request,'invalid.html', c)
	
def logout(request):
	c = {}
	c.update(csrf(request))
	return render(request,'index.html', c)
	
def otpvalid(request):
	c = {}
	c.update(csrf(request))
	temp=str(request.POST.get('otp',''))
	temp2=str(request.session['otps'])
	if temp==temp2:
		return render(request,'index.html',c)
	else:
		return render(request,'otpinvalid.html',c)
		