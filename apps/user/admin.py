from django.contrib import admin
from django.db import models

# Register your models here.
from user.models import CourseUser

class CourseUserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email','user_type', 'is_active', 'updated_at', )
	list_filter = ('created_at',)

# Register your models here.
admin.site.register(CourseUser, CourseUserAdmin)