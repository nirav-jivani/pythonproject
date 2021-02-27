from django import forms 

class imageupload(forms.Form): 
	file1 = forms.ImageField()
	file2 = forms.ImageField()
	file3 = forms.ImageField()
