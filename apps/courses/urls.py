from django.conf.urls import include, url
from apps.courses import views as courses_views

urlpatterns = [
    url(r'^$', courses_views.home, name='home'),    
    url(r'^courses/new/$', courses_views.new_course, name='new_course'),
    url(r'^courses/add/$', courses_views.add_courses, name='add_courses'),
        
    url(r'^modules/(?P<pk>[0-9]+)/$', courses_views.modules, name='modules'),
    url(r'^modules/new/(?P<pk>[0-9]+)/$', courses_views.modules_new, name='modules_new'),

    url(r'^modules/add/(?P<pk>[0-9]+)/$', courses_views.modules_add, name='modules_add'),
    
     

    url(r'^resource/new/$', courses_views.new_resource, name='new_resource'),
    url(r'^resource/add/$', courses_views.add_resource, name='add_resource'),
	
   

    url(r'^resources/(?P<pk>[0-9]+)/$', courses_views.resources, name='resources'),
    url(r'^resource/detail/(?P<pk>[0-9]+)/$', courses_views.resource_detail, name='resource_detail'),

   ]