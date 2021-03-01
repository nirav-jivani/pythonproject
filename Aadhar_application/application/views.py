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
# Create your views here.


def index(request):
	return render(request,'index.html');
	
def register(request):
	c = {}
	c.update(csrf(request))
	if(request.method == 'POST'):
		uname=request.session['uname']=request.POST['user']
		pass1=request.session['pass1']=request.POST['pass']
		pass3=request.POST['pass2']
		email=request.session['email']=request.POST['Email']
		num=request.POST['number']
		if(pass1 != pass3):
			messages.info(request,'Password does not match...')
			return redirect('/register')
		elif User.objects.filter(username=uname):
			messages.info(request,'username already exist..')
			return redirect('/register')
		elif User.objects.filter(last_name=num):
			messages.info(request,'username already exist..')
			return redirect('/register')
		else:
			return redirect('/verify')
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
	#client.messages.create(
	#body="your otp for for verfication is "+str(otp),
	#from_='+17084017359',
	#to=num1
	#)
	c = {}
	c.update(csrf(request))
	return render(request,'verification.html', c)
	
def check(request):
	c = {}
	c.update(csrf(request))
	user=request.POST.get('user','')
	password=request.POST.get('pass','')
	us=auth.authenticate(username=user,password=password);
	
	if us is not None:
		auth.login(request,us)
		return HttpResponseRedirect('logedin')
	else:
		messages.info(request,"invalid user name or password please enter valid details!!")
		return render(request,'index.html', c)
		
def logedin(request):
	c = {}
	c.update(csrf(request))
	return render(request,'logedin.html', c)

def invalid(request):
	c = {}
	c.update(csrf(request))
	return render(request,'invalid.html', c)
	
def logout(request):
	messages.info(request,"Logout successfully....  Thank you!!!!!")
	c = {}
	c.update(csrf(request))
	return render(request,'index.html', c)
	
def otpvalid(request):
	c = {}
	c.update(csrf(request))
	temp=str(request.POST.get('otp',''))
	temp2=str(request.session['otps'])
	user=User.objects.create_user(username=request.session['uname'],password=request.session['pass1'],email=request.session['email'],last_name=int(request.session['nums']))
	user.save()
	messages.info(request,'user created successfully..')
	return redirect('/')
	#else:
	#	return render(request,'otpinvalid.html',c)
		