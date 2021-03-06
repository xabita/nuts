from __future__ import unicode_literals

from django.db import models
from apps.users.models import UserCourse
from django.conf import settings



# DEPENDENCIES TO MAKE UNIQUE SLUG BY POST
#from autoslug import AutoSlugField
#from django.template.defaultfilters import slugify


CATEGORY_CHOICES = (
    (1, 'Texto'),
    (2, 'Codigo'),
    (3, 'Video'),
    (4, 'Audio'),
    (5, 'links')
)

# Create your models here.

class Course(models.Model):
	name= models.CharField(max_length=100)
	description = models.TextField()
	usercourse = models.ForeignKey('users.UserCourse', on_delete=models.CASCADE, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
#	slug = AutoSlugField( populate_from='name', max_length=100, always_update=True, unique=True)
	

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
	content = models.TextField()
	category = models.IntegerField(default = 1, choices=CATEGORY_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

class CourseStudent(models.Model):
	user_student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	course = models.ForeignKey('Course', on_delete=models.CASCADE, blank=True, null=False)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' % (self.user_student)

	def __unicode__(self):
		return self.user_student
		