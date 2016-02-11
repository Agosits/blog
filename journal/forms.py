from django import forms

class journal_form(forms.Form):
	title = forms.CharField(required=False)
	content = forms.CharField()
	tags = forms.CharField(required=False)

class comment_form(forms.Form):
	author = forms.CharField(required=True)
	email = forms.EmailField(required=False)
	content = forms.CharField()

class user_form(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)
	
	
