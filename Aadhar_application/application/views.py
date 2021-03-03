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
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.models import Session
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
		num=request.session['nums']=request.POST['number1']
		if(pass1 != pass3):
			messages.info(request,'Password does not match...')
			return redirect('/register')
		elif User.objects.filter(username=uname):
			messages.info(request,'username already exist..')
			return redirect('/register')
		elif User.objects.filter(last_name=num):
			messages.info(request,'mobile number already register...')
			return redirect('/register')
		else:
			return redirect('/verify')
	return render(request,'signup.html', c)

def verify(request):
	num=request.session['nums'];
	num1=("+91"+ str(num))
	id='ACed978f63efe65f095d94a2785e2c2555'
	token='be2bfd356cbf5c4825e8b4d0fa203773'
	client=Client(id,token)
	otp=random.randint(1000,9999)
	request.session['otps']=otp;
	client.messages.create(
	body="your otp for for verfication is "+str(otp),
	from_='+16789522224',
	to=num1
	)
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
	Session.objects.all().delete ()
	return render(request,'index.html', c)
	
def otpvalid(request):
	c = {}
	c.update(csrf(request))
	temp=str(request.POST.get('otp',''))
	temp2=str(request.session['otps'])
	if temp == temp2:
		user=User.objects.create_user(username=request.session['uname'],password=request.session['pass1'],email=request.session['email'],last_name=int(request.session['nums']))
		user.save()
		messages.info(request,'user created successfully..')
		del request.session['otps']
		return redirect('/')
	else:
		return render(request,'otpinvalid.html',c)

def forgot(request):
	c = {}
	c.update(csrf(request))
	if (request.method == 'POST'):
		if 'otps1' not in request.session:
			num=request.POST['number']
			if User.objects.filter(last_name=num): 
				request.session['number']=request.POST['number']
				return redirect('/send')
			else:
				messages.info(request,"user can not found please register...")
				te=num
				return render(request,'forgot.html',{'temp':te})
		else:
			otp1=str(request.POST['otp'])
			otp2=str(request.session['otps1'])
			if otp1 != otp2:
				te=request.session['number']
				messages.info(request,'please enter valid otp...')
				return render(request,'forgot.html',{'temp':te})
			else:
				del request.session['otps1']
				return render(request,'newuserpass.html',c)
	return render(request,'forgot.html',c)

def send(request):
	num=request.session['number']
	num1="+91"+str(num)
	id='ACed978f63efe65f095d94a2785e2c2555'
	token='be2bfd356cbf5c4825e8b4d0fa203773'
	client=Client(id,token)
	otp=random.randint(1000,9999)
	request.session['otps1']=otp;
	client.messages.create(
	body="your otp for for verfication is "+str(otp),
	from_='+16789522224',
	to=num1
	)
	c = {}
	c.update(csrf(request))
	messages.info(request,"otp send successfully....")
	te=request.session['number']
	return render(request,'forgot.html',{'temp':te})

def reset(request):
	c = {}
	c.update(csrf(request))
	num=request.session['number']
	uname=request.POST['user']
	pass1=request.POST['pass']
	pass3=request.POST['pass2']
	if(pass1 != pass3):
		messages.info(request,'Password does not match...')
		return render(request,'newuserpass.html',c)
	elif User.objects.filter(username=uname):
		messages.info(request,'username already exist..')
		return render(request,'newuserpass.html',c)
	else:
		us=User.objects.get(last_name=num)
		us.username=uname
		us.password=make_password(pass1)
		us.save()
		messages.info(request,"user name or password reset successfully....")
		return redirect('/')

	


		