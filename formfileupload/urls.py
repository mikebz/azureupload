from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chunked/$', views.chunked, name='chunked'),
    url(r'^signature/(?P<file_name>[\w\-\. ]+)$', views.signature, name='signature')
]