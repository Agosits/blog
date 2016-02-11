from django.db import models

# Create your models here.
class journal(models.Model):
	"""docstring for journal
	This is the object of journal"""
	#sid = models.AutoField(primary_key=True)
	title = models.CharField(max_length=1000)
	time = models.DateField(max_length=1000)
	content = models.TextField()
	tags = models.CharField(max_length=1000,default="")

	def __str__(self):
		return self.title
'''class user(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.username'''

class comment(models.Model):
	"""docstring for comment"""
	author = models.CharField(max_length=100,blank=False,default="foobar")
	email = models.EmailField()
	content = models.TextField()

	def __str__(self):
		return self.author

class tag(models.Model):
	name = models.CharField(max_length=100)
	journals = models.CharField(max_length=1000)

	def __str__(self):
		return self.name

class mid(models.Model):
	maxid = models.IntegerField()

	def __str__(self):
		return self.maxid

		

		