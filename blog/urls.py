from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='blog.index'),
    url(r'^(?P<id>\d+)/$', views.post, name='blog.post'),
    url(r'^add/$', views.add_post, name='blog.add_post'),
    url(r'^(?P<id>\d+)/edit/$', views.edit_post, name='blog.edit_post'),
    url(r'^delete/$', views.delete_post, name='blog.delete_post'),
    url(r'^all/$', views.all, name='blog.all'),
]
