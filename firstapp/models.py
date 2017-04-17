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
    # foreign key:
    # ID = models.ForeignKey('studentID')
    def __str__(self):
        return self.name


class Article(models.Model):
    headline = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.headline
    def __unicode__(self):
        return self.headline