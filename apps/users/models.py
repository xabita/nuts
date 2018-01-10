from django.db import models

class UserCourse(models.Model):
	first_name = models.CharField(max_length=60 ,blank=True, null=True)
	last_name = models.CharField(max_length=60 ,blank=True, null=True)
	email = models.EmailField(default='mail@co.co', blank=False)
	user_type= models.IntegerField(default = 2)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.first_name

	def __unicode__(self):
		return self.first_name