from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import ListView, DetailView
from app.models import location, photo, media



# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'title': 'index'
        })
    return HttpResponse(template.render(context))

def about(request):
    template = loader.get_template('about.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))



def gallery(request):
    template = loader.get_template('gallery.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

class LookHereView(ListView):
    template_name = 'gallery.html'
    model=location

    def get_context_data(self, **kwargs):
        context = super(LookHereView, self).get_context_data(**kwargs)
        context['landscapes'] =  location.objects.filter(architecture="L")
        context['hardscapes'] = location.objects.filter(architecture="H")
        return context

class LandScapeView(ListView):
    template_name = 'location.html'
    model = location

    def get_context_data(self, **kwargs):
        context = super(LandScapeView, self).get_context_data(**kwargs)
        context['landscapes'] =  location.objects.filter(architecture="L")
        context['hardscapes'] = location.objects.filter(architecture="H")
        photos = photo.objects.filter(Splash="L").order_by('order')
        context['photos'] = photos
        context['title'] = 'LANDSCAPES'
        return context

class HardScapeView(ListView):
    template_name = 'location.html'
    model = location

    def get_context_data(self, **kwargs):
        context = super(HardScapeView, self).get_context_data(**kwargs)
        context['landscapes'] =  location.objects.filter(architecture="L")
        context['hardscapes'] = location.objects.filter(architecture="H")
        photos = photo.objects.filter(Splash="H").order_by('order')
        context['photos'] = photos
        context['title'] = 'HARDSCAPES'
        return context


class MediaView(ListView):
    template_name = 'media.html'
    model = media

    def get_context_data(self, **kwargs):
        context = super(MediaView, self).get_context_data(**kwargs)
        context['landscapes'] =  location.objects.filter(architecture="L")
        context['hardscapes'] = location.objects.filter(architecture="H")
        context['media'] = media.objects.all().order_by('order')
        return context


class LocationView(DetailView):
    template_name = 'location.html'
    model = location
    slug_field = 'slug_url'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        self.location = get_object_or_404(location, slug_url=self.kwargs['name'])
        context['photos'] = photo.objects.filter(location=self.location)
        context['landscapes'] =  location.objects.filter(architecture="L")
        context['hardscapes'] = location.objects.filter(architecture="H")
        context['location'] = self.location
        context['title'] = self.location.name
        return context

class PhotoView(DetailView):
    template_name= 'photo.html'
    model = photo
    slug_field = "slug_url"
    slug_url_kwarg = "photo_name"

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(*kwargs)
        self.photo = get_object_or_404(photo, order=self.kwargs['photo_number'])
        return context


