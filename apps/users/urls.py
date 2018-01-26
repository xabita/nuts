from django.conf.urls import include, url
from apps.users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [

    
   # url(r'^login/$', auth_views.login, name='login'),
   # url(r'^logout/$', auth_views.logout, name='logout'),
   
    
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    #url(r'^logout/$', user_views.logoutUs, name='logoutUs'),



    url(r'^users/$', user_views.home_users, name='home_users'),    
    url(r'^users/new/$', user_views.users_new, name='users_new'),
    url(r'^users/add/$', user_views.users_add, name='users_add'),
        
    #url(r'^modules/(?P<pk>[0-9]+)/$', courses_views.modules, name='modules'),
    #url(r'^modules/new/(?P<pk>[0-9]+)/$', courses_views.modules_new, name='modules_new'),
    #url(r'^modules/add/(?P<pk>[0-9]+)/$', courses_views.modules_add, name='modules_add'),
   ]