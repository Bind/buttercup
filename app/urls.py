from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name="about"),
    url(r'^location/(?P<name>[\w-]+)/$', views.LocationView.as_view()),
    url(r'^look_here/', views.LookHereView.as_view()),
    )