from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class course(models.Model):
    compulsory = models.BooleanField(default='False')
    name = models.CharField(max_length=100)
    sid = models.CharField(max_length=20)
    grades = models.CharField(max_length=100)
    power = models.IntegerField(null=True)
    time = models.IntegerField(default=0)
    classroom = models.CharField(max_length=10,default='0-000')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('sid',)


class student(models.Model):
    name = models.CharField(max_length=100)
    sid = models.CharField(max_length=12)
    cla = models.CharField(max_length=10)
    timetable = models.IntegerField(default=0)
    courses = models.ManyToManyField(course,blank=True)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('sid',)

'''class teacher(models.Model):
    sid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    clas = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)

    def __str__(self):
        return self.name'''

class grade(models.Model):
    name = models.CharField(max_length=10)
    courses = models.ManyToManyField(course)

    def __str__(self):
        return self.name