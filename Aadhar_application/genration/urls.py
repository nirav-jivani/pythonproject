from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
	path('genre',views.genre),
	path('genreadhar',views.genreadhar),
	path('uidisplay',views.displaynumber),
	path('uidisplay',views.displaynumber),
	path('genremaster',views.genremaster),
	path('send2',views.send2),
	]