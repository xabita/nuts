# urls.py
from django.conf.urls import include, url
from apps.faqs import views as faqs_views


urlpatterns = [
    url(r'^comments/add/$', faqs_views.add_comments, name='add_comments'),
]