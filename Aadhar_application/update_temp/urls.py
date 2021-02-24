from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
	path('updateinfo',views.updateinfo),
	path('updatelist',views.updatelist),
	path('updatename',views.updatename),
	path('validname',views.validname),
	path('updateDOB',views.updateDOB),
	path('validDOB',views.validDOB),
	path('updateadd',views.updateadd),
	path('validadd',views.validadd),
	path('updatephoto',views.updatephoto),
	path('validphoto',views.validphoto),
	]