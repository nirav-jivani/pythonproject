from django.db import models

# Create your models here.

class newapp(models.Model):
	name=models.CharField(max_length=20)
	gender=models.CharField(max_length=10)
	address=models.CharField(max_length=100)
	relationtype=models.CharField(max_length=20)
	relativename=models.CharField(max_length=20)
	birthaddress=models.CharField(max_length=20)
	birthdate=models.DateField(max_length=20)
	number=models.BigIntegerField()
	email=models.EmailField()
	rdate=models.DateField(max_length=20)
	fdate=models.DateField(max_length=20)
	place=models.CharField(max_length=20)
	addfname=models.CharField(max_length=20,null=True)
	agefname=models.CharField(max_length=20,null=True)
	addf=models.ImageField(null=True,blank=True,upload_to="images/address_proof/")
	agef=models.ImageField(null=True,blank=True,upload_to="images/age_proof/")
	phf=models.ImageField(null=True,blank=True,upload_to="images/photograph/")
	vid=models.BigIntegerField()
	class Meta:
		db_table="user_details"

