from django.contrib import admin
from app.models import location, photo, media


class PhotoInline(admin.StackedInline):
    model = photo
    extra = 5

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name','location','Splash', 'order' )
class LocationAdmin(admin.ModelAdmin):

    inlines = [PhotoInline]

admin.site.register(photo, PhotoAdmin)
admin.site.register(media)
admin.site.register(location, LocationAdmin)



# Register your models here.
