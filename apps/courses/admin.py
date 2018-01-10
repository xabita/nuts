from django.contrib import admin
from django.db import models

# Register your models here.
from apps.courses.models import Course, CourseModule, Resource

class CourseAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'updated_at', )
	list_filter = ('created_at',)

class CourseModuleAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'objective', 'time', 'updated_at', )
	list_filter = ('created_at',)

class ResourceAdmin(admin.ModelAdmin):
	list_display = ('title', 'url_video', 'courseModule', 'description', 'updated_at', )



# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseModule, CourseModuleAdmin)
admin.site.register(Resource, ResourceAdmin)