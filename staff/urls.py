__author__ = 'coffe67'
from django.conf.urls import url, include
from django.contrib import admin
import views as staff_views
admin.autodiscover()

urlpatterns = [
    url(r'^$', staff_views.staff_login, name='staff_login'),
    url(r'^signup/', staff_views.staff_signup, name='staff_signup'),
    url(r'^staff/logout$', staff_views.staff_logout, name='staff_logout'),
    url(r'^staff/', include('seeds.urls')),
]
