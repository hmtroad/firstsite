from __future__ import unicode_literals

from django.db import models

# Create your models here.


class People(models.Model):
    # blank is for form, null is for database
    name = models.CharField(null=True, blank=False, max_length=100)
    gender = models.CharField(null=True, blank=True, max_length=10)
    major = models.CharField(null=True, blank=True, max_length=10)
    grade = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True,blank=False)
    password = models.CharField(null=True, blank=False,max_length=16)
    phone = models.CharField(null=True, blank=True, max_length=100)
    # foreign key:
    # ID = models.ForeignKey('studentID')
    def __str__(self):
        return self.name

class Association(models.Model):
    asc_name = models.CharField(null= True, blank = True, max_length = 200)
    asc_id = models.CharField(null= True, blank = True, max_length = 200)

class Activity(models.Model):
    hoster = models.ForeignKey(Association, on_delete=models.CASCADE)
    act_name = models.CharField(null= True, blank = True, max_length = 200)
    act_address = models.CharField(null = True, blank = True, max_length = 200)
    introduction = models.CharField(null = True, blank = True, max_length=500)

class Passage(models.Model):
    content = models.CharField(null=True, blank=True, max_length=200)
    title = models.CharField(null=True, blank=True, max_length=200)
    writer = models.TextField(null=True, blank=True)

class Inform(models.Model):
    sender = models.ForeignKey(People, on_delete=models.CASCADE)
    accepter = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

class MememberOf(models.Model):
    member = models.ForeignKey(People)
    assoc = models.ForeignKey(Association)
    role = models.CharField(null=True, blank=True, max_length=200)

#Apply For
class ApplyFor(models.Model):
    member = models.CharField(null=True, blank=True, max_length = 200)
    assoc = models.CharField(null=True, blank=True, max_length=200)
    apply_time = models.DateField(null=True, blank=True)
