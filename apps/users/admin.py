from django.contrib import admin
from django.db import models

# Register your models here.
from apps.users.models import UserCourse

class UserCourseAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email','user_type', 'is_active', 'updated_at', )

# Register your models here.
admin.site.register(UserCourse, UserCourseAdmin)