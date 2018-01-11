from django.conf.urls import include, url
from apps.courses import views as courses_views


urlpatterns = [
    url(r'^$', courses_views.home, name='home'),
    
    url(r'^courses/new/$', courses_views.new_course, name='new_course'),
    url(r'^courses/add/$', courses_views.add_courses, name='add_courses'),


   ]