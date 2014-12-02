from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name="about"),
    url(r'^media/', views.MediaView.as_view()),
    url(r'^location/(?P<name>[\w-]+)/$', views.LocationView.as_view()),
    url(r'^hardscapes/', views.HardScapeView.as_view()),
    url(r'^landscapes/', views.LandScapeView.as_view()),
    url(r'^location/(?P<name>[\w-]+)/(?P<photo_number>[\w-]+)/$', views.PhotoView.as_view()),
    )