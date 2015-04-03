from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import ListView, DetailView
from app.models import location, photo, media, landscape, hardscape
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60*15)
def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'title': 'index',
        'index':'index'
        })
    return HttpResponse(template.render(context))

@cache_page(60*15)
def about(request):
    template = loader.get_template('about.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

@cache_page(60*15)
def contact(request):
    template = loader.get_template('contact.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

class LandScapeView(ListView):
    template_name = 'location.html'
    model = landscape
    paginate_by = 6
    context_object_name = "landscapes"

    def get_context_data(self, **kwargs):
        context = super(LandScapeView, self).get_context_data(**kwargs)
        context['title'] = 'LANDSCAPES'
        context["prefix"] = 'landscape'
        return context

class HardScapeView(ListView):
    template_name = 'location.html'
    model = hardscape
    paginate_by = 6
    context_object_name = "landscapes"

    def get_context_data(self, **kwargs):
        context = super(HardScapeView, self).get_context_data(**kwargs)
        context['title'] = 'HARDSCAPES'
        context["prefix"] = 'hardscape'
        return context

class MediaView(ListView):
    template_name = 'media.html'
    model = media
    paginate_by = 6
    context_object_name = "media"


class landscapeDetailView(ListView):
    template_name = 'gallery.html'
    model = photo
    slug_field = 'slug_url'
    slug_url_kwarg = 'name'
    paginate_by = 6
    context_object_name = 'photos'

    def get_queryset(self):
        queryset = super(landscapeDetailView, self).get_queryset()
        queryset = queryset.filter(landscape__slug_url=self.kwargs['name'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(landscapeDetailView, self).get_context_data(**kwargs)
        self.location = get_object_or_404(landscape, slug_url=self.kwargs['name'])
        context['location'] = self.location
        context['title'] = self.location.name
        context['prefix'] = "landscape"
        return context

class hardscapeDetailView(ListView):
    template_name = 'gallery.html'
    model = photo
    slug_field = 'slug_url'
    slug_url_kwarg = 'name'
    paginate_by = 6
    context_object_name = 'photos'

    def get_queryset(self):
        queryset = super(hardscapeDetailView, self).get_queryset()
        queryset = queryset.filter(hardscape__slug_url=self.kwargs['name'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(hardscapeDetailView, self).get_context_data(**kwargs)
        self.location = get_object_or_404(hardscape, slug_url=self.kwargs['name'])
        context['location'] = self.location
        context['title'] = self.location.name
        context['prefix'] = "hardscape"
        return context

class hardscapePhotoView(DetailView):
    template_name= 'photo.html'
    model = photo
    slug_field = "slug_url"
    slug_url_kwarg = "photo_number"
    context_object_name = "photo"

    def get_queryset(self):
        queryset = super(hardscapePhotoView, self).get_queryset()
        queryset.select_related('next_photo_hardscape', 'prev_photo_hardscape', 'hardscape').filter(slug_url=self.kwargs['photo_number'])
        return queryset.distinct()


    def get_context_data(self, **kwargs):
        context = super(hardscapePhotoView, self).get_context_data(**kwargs)
        context['next'] = context['photo'].next_photo_hardscape
        context['prev'] = context['photo'].prev_photo_hardscape
        context['prefix'] = "hardscape"
        context["company"] = context['photo'].hardscape
        return context

class landscapePhotoView(DetailView):
    template_name= 'photo.html'
    model = photo
    slug_field = "slug_url"
    slug_url_kwarg = "photo_number"
    context_object_name = "photo"

    def get_queryset(self):
        queryset = super(landscapePhotoView, self).get_queryset()
        queryset.select_related('next_photo_landscape', 'prev_photo_landscape', 'landscape').filter(slug_url=self.kwargs['photo_number'])
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super(landscapePhotoView, self).get_context_data(**kwargs)

        context['prefix'] = "landscape"
        context['next'] = context['photo'].next_photo_landscape
        context['prev'] = context['photo'].prev_photo_landscape
        """context['photos'] = self.photo.landscape.get_photos"""
        context["company"] = context['photo'].landscape
        return context


