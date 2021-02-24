from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
	path('new_form',views.address),
	path('dob',views.dob),
	path('personal',views.personal),
	path('dec',views.declaration),
	path('proof',views.proof),
	path('preview',views.preview),
	path('submitform',views.submitform),
	]