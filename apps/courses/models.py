from django.db import models
from apps.users.models import UserCourse
# Create your models here.

class Course(models.Model):
	name= models.CharField(max_length=100)
	description = models.TextField()
	usercourse = models.ForeignKey('users.UserCourse', on_delete=models.CASCADE, blank=True, null=True)
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

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name
		

class Resource(models.Model):
	title = models.CharField(max_length=100)
	url_video = models.URLField(default="")
	courseModule = models.ForeignKey('CourseModule', on_delete=models.CASCADE, blank = True, null = True)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title