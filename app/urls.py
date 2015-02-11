from django.conf.urls import include, patterns, url
from django.conf import settings
from app import views
from django.views.decorators.cache import cache_page

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name="about"),
    url(r'^media/', views.MediaView.as_view()),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^hardscape/(?P<name>[\w-]+)/$', cache_page(6000*15)(views.hardscapeDetailView.as_view())),
    url(r'^landscape/(?P<name>[\w-]+)/$', cache_page(6000*15)(views.landscapeDetailView.as_view())),
    url(r'^hardscapes/', cache_page(6000*15)(views.HardScapeView.as_view())),
    url(r'^landscapes/', cache_page(6000*15)(views.LandScapeView.as_view())),
    url(r'^hardscape/(?P<name>[\w-]+)/(?P<photo_number>[\w-]+)/$',cache_page(6000*15)( views.hardscapePhotoView.as_view())),
    url(r'^landscape/(?P<name>[\w-]+)/(?P<photo_number>[\w-]+)/$', cache_page(6000*15)(views.landscapePhotoView.as_view())),
    )


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )