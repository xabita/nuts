from django.contrib import admin
from django.db import models

# Register your models here.
from course.models import Course, CourseModule

class CourseAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'updated_at', )
	list_filter = ('created_at',)

class CourseModuleAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'objective', 'time', 'updated_at', )
	list_filter = ('created_at',)
CourseModule

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseModule, CourseModuleAdmin)