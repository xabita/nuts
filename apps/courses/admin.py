from django.contrib import admin
from django.db import models

# Admin Pagedown Widget
from pagedown.widgets import AdminPagedownWidget


from .forms import CourseForm, CourseModuleForm, ResourceForm

# Register your models here.
from apps.courses.models import Course, CourseModule, Resource

class CourseAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'updated_at', )
	list_filter = ('created_at',)

class CourseModuleAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'objective', 'time', 'updated_at', )
	list_filter = ('created_at',)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    form = ResourceForm
    fields = ('title', 'url_video', 'courseModule','content', 'category', )
	#list_display = ('title', 'url_video', 'courseModule','content', 'category', 'updated_at',  )
	#formfield_overrides = {
    #    models.TextField: {'widget': AdminPagedownWidget },
    #}


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseModule, CourseModuleAdmin)
#admin.site.register(Resource, ResourceAdmin)