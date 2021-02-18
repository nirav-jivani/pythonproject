from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
	path('new_Aadhar/new_form',views.address),
	path('new_Aadhar/dob',views.dob),
	path('new_Aadhar/personal',views.personal),
	path('new_Aadhar/dec',views.declaration),
	path('new_Aadhar/proof',views.proof),
	]