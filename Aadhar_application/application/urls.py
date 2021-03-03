from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
	path('',views.index),
	path('index',views.index),
	path('register',views.register),
	path('verify',views.verify),
	path('check',views.check),
	path('logedin',views.logedin),
	path('invalid',views.invalid),
	path('logout',views.logout),
	path('otpvalid',views.otpvalid),
	path('forgot',views.forgot),
	path('send',views.send),
	path('reset',views.reset),
	]