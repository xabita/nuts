from django.conf.urls import include, url
from apps.courses import views as courses_views

urlpatterns = [
    url(r'^$', courses_views.home, name='home'),    
    url(r'^courses/new/$', courses_views.new_course, name='new_course'),
    url(r'^courses/add/$', courses_views.add_courses, name='add_courses'),
    url(r'^courses/for_teacher/(?P<pk>[0-9]+)/$', courses_views.my_courses, name='my_courses'),
        
    url(r'^modules/(?P<pk>[0-9]+)/$', courses_views.modules, name='modules'),
    url(r'^modules/new/(?P<pk>[0-9]+)/$', courses_views.modules_new, name='modules_new'),
    url(r'^modules/add/(?P<pk>[0-9]+)/$', courses_views.modules_add, name='modules_add'),
    
    url(r'^resources/(?P<pk>[0-9]+)/$', courses_views.resources, name='resources'),
     

    url(r'^resource/new/(?P<pk>[0-9]+)/$', courses_views.resource_new, name='resource_new'),
    url(r'^resource/add/(?P<pk>[0-9]+)/$', courses_views.resource_add, name='resource_add'),
    url(r'^resource/detail/(?P<pk>[0-9]+)/$', courses_views.resource_detail, name='resource_detail'),

    url(r'^student/new/$', courses_views.student_new, name='student_new'),
    url(r'^student/add/(?P<studentId>\w+)/(?P<courseId>\w+)/$', courses_views.student_add, name='student_add'),
            
   ]