from django.db import models

# Create your models here.
class CourseUser(models.Model):
	name = models.CharField(max_length=100 ,blank=True, null=True)
	email = models.EmailField(default='mail@co.co', blank=False)
	user_type= models.IntegerFiel(default = 3)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

