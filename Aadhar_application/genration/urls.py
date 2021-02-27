from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
	path('genre',views.genre),
	path('genreadhar',views.genreadhar),
	path('uidisplay',views.displaynumber),
	]