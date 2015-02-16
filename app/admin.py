from django.contrib import admin
from app.models import location, photo, media, landscape, hardscape


class PhotoInline(admin.StackedInline):
    model = photo
    extra = 5

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name','location','hero', 'order','slug_url' )

class LocationAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('name', 'architecture')
    list_editable = ('architecture',)

class LandscapeAdmin(admin.ModelAdmin):
        inlines = [PhotoInline]
        list_display = ('name','order')
        list_editable = ('order',)

class HardscapeAdmin(admin.ModelAdmin):
        list_display = ('name',)
        inlines = [PhotoInline]

class MediaAdmin(admin.ModelAdmin):
        list_display = ('order')
        list_editable = ('order')



admin.site.register(landscape, LandscapeAdmin)
admin.site.register(hardscape, HardscapeAdmin)
admin.site.register(photo, PhotoAdmin)
admin.site.register(media, MediaAdmin)
admin.site.register(location, LocationAdmin)



# Register your models here.
