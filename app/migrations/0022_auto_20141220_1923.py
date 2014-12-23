# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def movePhotos(apps, schema_editor):
    Location = apps.get_model('app', "location")
    Landscape = apps.get_model('app', 'landscape')
    Hardscape = apps.get_model('app', 'hardscape')
    Photo = apps.get_model('app', "photo")
    for loc in Location.objects.all():
        if loc.architecture == "L":
            for pic in loc.pictures:   
                pic.landscape = Landscape.filter(name=loc.name) 
        if loc.architecture == "H":
            for pic in loc.pictures:
                pic.hardscape = Hardscape.filter(name=loc.name) 



class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20141220_1923'),
    ]

    operations = [
    migrations.RunPython(movePhotos),
    ]
