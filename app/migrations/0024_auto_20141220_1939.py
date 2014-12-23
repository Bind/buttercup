from __future__ import unicode_literals

from django.db import models, migrations

def movePhotos(apps, schema_editor):
    Location = apps.get_model('app', "location")
    Landscape = apps.get_model('app', 'landscape')
    Hardscape = apps.get_model('app', 'hardscape')
    Photo = apps.get_model('app', "photo")
    for loc in Location.objects.all():
        if loc.architecture == "L":
            for pic in loc.pictures.all():   
                pic.landscape = Landscape.objects.get(name=loc.name)
                pic.save()
        if loc.architecture == "H":
            for pic in loc.pictures.all():
                pic.hardscape = Hardscape.objects.get(name=loc.name)
                pic.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20141220_1935'),
    ]

    operations = [
    migrations.RunPython(movePhotos),
    ]
