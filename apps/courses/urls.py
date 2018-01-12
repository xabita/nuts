from django.conf.urls import include, url
from apps.courses import views as courses_views

urlpatterns = [
    url(r'^$', courses_views.home, name='home'),    
    url(r'^courses/new/$', courses_views.new_course, name='new_course'),
    url(r'^courses/add/$', courses_views.add_courses, name='add_courses'),
    url(r'^course_module/new/$', courses_views.new_course_module, name='new_course_module'),
    url(r'^course_module/add/$', courses_views.add_course_module, name='add_course_module'),
    url(r'^resource/new/$', courses_views.new_resource, name='new_resource'),
    url(r'^resource/add/$', courses_views.add_resource, name='add_resource'),
	url(r'^course/detail/$', courses_views.course_detail, name='course_detail'),


   ]