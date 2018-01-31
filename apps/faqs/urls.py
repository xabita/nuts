# urls.py
from django.conf.urls import include, url
from faqs import views as faqs_views


urlpatterns = [
    url(r'^comments/add/$', faqs_views.add_comments, name='add_comments'),
    url(r'^comments/add_resource/$', faqs_views.add_comments_resource, name='add_comments_resource'),
]