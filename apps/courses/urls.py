from django.conf.urls import include, url
from courses import views as courses_views


urlpatterns = [
    url(r'^$', courses_views.home, name='home'),
   ]