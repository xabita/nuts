from django.db import models

# Create your models here.

class Course(models.Model):
	name= models.CharField(max_length=100)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class CourseModule(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	objective = models.TextField
	timing = models.CharField(100);
	course = models.ForeignKey('Course', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Resource(models.Model):
	title = models.CharField(max_length=100)
	courseModule = models.ForeignKey('CourseModule', blank = True, null = True)
	escription = models.TextField()
