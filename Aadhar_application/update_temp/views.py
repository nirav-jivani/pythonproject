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

def updateinfo(request):
	c = {}
	c.update(csrf(request))
	if 'otps2' not in request.session:
		messages.info(request,"Master otp not set please set it..")
		return render(request,"logedin.html",c)
	return render(request,'updateinfo.html',c)

def updatelist(request):
	c = {}
	c.update(csrf(request))
	number1=request.POST['number']
	uid=request.POST['anum']
	otp1=str(request.POST['msotp'])
	otp2 = str(request.session['otps2'])
	if otp1 != otp2 :
		messages.info(request,"invalid master otp....")
		return render(request,'updateinfo.html',c)
	else:
		try:
			s1=newapp.objects.get(id=uid,number=number1)
			request.session['uid']=uid
			return render(request,'updatelist.html',c)
		except:
			messages.info(request,'invalid details please enter valid details')
			return render(request,'logedin.html',c)

def updatename(request):
	c = {}
	c.update(csrf(request))
	return render(request,'updatename.html',c)

def validname(request):
	name1=request.POST['name']+request.POST['surname']
	gen=request.POST['gender']
	s1=newapp.objects.get(id=request.session['uid'])
	s1.name=name1
	s1.gender=gen
	s1.save()
	messages.info(request,"name updated successfully...  thank you!!")
	c = {}
	c.update(csrf(request))
	return render(request,'updatelist.html',c)

def updateDOB(request):
	c = {}
	c.update(csrf(request))
	test={}
	test['form1']=imageupload();
	return render(request,'updateDOB.html',test)

def validDOB(request):
	dob=request.POST['udate']
	tp=request.POST['agep']
	test2=imageupload(request.POST,request.FILES)
	st=newapp.objects.get(id=request.session['uid'])
	st.birthdate=dob
	st.agefname=tp
	st.agef=request.FILES['file1']
	st.save()
	messages.info(request,"Date of Birth updated successfully...  thank you!!")
	c = {}
	c.update(csrf(request))
	return render(request,'updatelist.html',c)

def updateadd(request):
	c = {}
	c.update(csrf(request))
	test={}
	test['form1']=imageupload();
	return render(request,'updateadd.html',test)

def validadd(request):
	address1=(request.POST['house'] + "- " + request.POST['area'] +" " + request.POST['tv'] + " " + request.POST['dist']
						   +" " +request.POST['state'] +" "+request.POST['pincode'])
	rdate1=request.POST['date']
	adp1=request.POST['adp']
	test2=imageupload(request.POST,request.FILES)
	st=newapp.objects.get(id=request.session['uid'])
	st.address=address1
	st.addfname=adp1
	st.rdate=rdate1
	st.addf=request.FILES['file1']
	st.save()
	messages.info(request,"Address updated successfully...  thank you!!")
	c = {}
	c.update(csrf(request))
	return render(request,'updatelist.html',c)

def updatephoto(request):
	c = {}
	c.update(csrf(request))
	test={}
	test['form1']=imageupload();
	return render(request,'updatephoto.html',test)

def validphoto(request):
	test2=imageupload(request.POST,request.FILES)
	st=newapp.objects.get(id=request.session['uid'])
	st.phf=request.FILES['file1']
	st.save()
	messages.info(request,"Photo updated successfully...  thank you!!")
	c = {}
	c.update(csrf(request))
	return render(request,'updatelist.html',c)