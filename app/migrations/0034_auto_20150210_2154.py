# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def processImages(apps, schema_editor):
    Photo = apps.get_model("app", "photo")
    for photo in Photo.objects.all():
        photo.display_opt = photo.display
        photo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20150108_2210'),
    ]

    operations = [migrations.RunPython(processImages)
    ]
