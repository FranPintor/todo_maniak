__author__ = 'coffe67'
from django.conf.urls import url
from django.contrib import admin
import views as seeds_views
admin.autodiscover()

urlpatterns = [
    url(r'^$', seeds_views.todo_list, name='todo_list'),
    url(r'^create/$', seeds_views.todo_create, name='todo_create'),
    url(r'^detail/(?P<slug>[-\w]+)', seeds_views.todo_detail, name='todo_detail'),
    url(r'^delete/logout$', seeds_views.todo_delete, name='todo_delete'),
    url(r'^assign/(?P<todo_id>[-\w]+)', seeds_views.todo_assign, name='todo_assign'),
    url(r'^completed/$', seeds_views.todo_completed, name='todo_completed'),
]