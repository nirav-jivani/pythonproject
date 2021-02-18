from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth ,messages
from django.contrib.auth.models import auth ,User
from django.template.context_processors import csrf

# Create your views here.

def address(request):
	c = {}
	c.update(csrf(request))
	return render(request,'new_aadhar.html', c)
	
def dob(request):
	c = {}
	c.update(csrf(request))
	return render(request,'dob.html', c)

def personal(request):
	c = {}
	c.update(csrf(request))
	return render(request,'personal.html', c)
	
def declaration(request):
	c = {}
	c.update(csrf(request))
	return render(request,'dec.html', c)

def proof(request):
	c = {}
	c.update(csrf(request))
	return render(request,'proof.html', c)