from django.db import models

#from django.nuts.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager





USER_CHOICES = (
    (1, 'Administrador'),
    (2, 'Instructor'),
    (3, 'Estudiante'),
)
   
class UserCourse(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(max_length=60 ,blank=True, null=False)
	last_name = models.CharField(max_length=60 ,blank=True, null=False)
	email = models.EmailField(default='mail@co.co', blank=False, unique=True)
	user_type= models.IntegerField(default = 3, choices=USER_CHOICES)
	is_active = models.BooleanField(default=True)
	username = models.CharField(max_length=15 ,blank=True, null=False, unique=True)
	password = models.CharField(max_length=150,blank=True, null=False)
	last_login = models.DateTimeField(auto_now=True)
	is_staff = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')
	def get_full_name(self):
		'''Returns the first_name plus the last_name, with a space in between.'''
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()
	def get_short_name(self):
		'''Returns the short name for the user.'''
		return self.first_name

	def email_user(self, subject, message, from_email=None, **kwargs):
		'''Sends an email to this User.'''
		send_mail(subject, message, from_email, [self.email], **kwargs)


	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)


	def __unicode__(self):
		return self.first_name