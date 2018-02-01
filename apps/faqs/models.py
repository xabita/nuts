from django.db import models

from apps.courses.models import Resource
from apps.users.models import UserCourse

# Faqs Model
class ResourceComment(models.Model):
	comment= models.TextField()
	resource= models.ForeignKey(Resource, on_delete=models.CASCADE, blank=False, null=False)
	usercourse = models.ForeignKey('users.UserCourse', on_delete=models.CASCADE, blank=False, null=False)
	is_published = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	