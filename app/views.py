from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import ListView, DetailView
from app.models import location, photo




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


def media(request):
    template = loader.get_template('media.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))




def gallery(request):
    template = loader.get_template('gallery.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))



class LocationView(ListView):
    template_name = 'gallery.html'

    def get_queryset(self):
        self.location = get_object_or_404(location, name=self.args)
        return photo.objects.filter(location=self.location)

    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['location'] = self.location
        return context