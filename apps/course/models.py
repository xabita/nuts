from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Course(models.Model):
	name= models.CharField(max_length=100)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class CourseModule(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	objective = models.TextField()
	time = models.CharField(max_length=100)
	course = models.ForeignKey('Course', on_delete=models.CASCADE, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
'''
class Resource(models.Model):
	title = models.CharField(max_length=100)
	courseModule = models.ForeignKey('CourseModule', blank = True, null = True)
	description = models.TextField()
'''
