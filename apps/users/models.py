from django.db import models


USER_CHOICES = (
    (1, 'Administrador'),
    (2, 'Instructor'),
    (3, 'Estudiante'),
)
   
class UserCourse(models.Model):
	first_name = models.CharField(max_length=60 ,blank=True, null=True)
	last_name = models.CharField(max_length=60 ,blank=True, null=True)
	email = models.EmailField(default='mail@co.co', blank=False)
	user_type= models.IntegerField(default = 3, choices=USER_CHOICES)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)


	def __unicode__(self):
		return self.first_name