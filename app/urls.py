from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name="about"),
    url(r'^media/', views.MediaView.as_view()),
    url(r'^hardscape/(?P<name>[\w-]+)/$', views.hardscapeDetailView.as_view()),
    url(r'^landscape/(?P<name>[\w-]+)/$', views.landscapeDetailView.as_view()),
    url(r'^hardscapes/', views.HardScapeView.as_view()),
    url(r'^landscapes/', views.LandScapeView.as_view()),
    url(r'^hardscape/(?P<name>[\w-]+)/(?P<photo_number>[\w-]+)/$', views.hardscapePhotoView.as_view()),
    url(r'^landscape/(?P<name>[\w-]+)/(?P<photo_number>[\w-]+)/$', views.landscapePhotoView.as_view()),
    )