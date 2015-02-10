# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models
import imagekit.models.fields


def processImages(apps, schema_editor):
    Photo = apps.get_model("app", "photo")
    for photo in Photo.objects.all():
        photo.display_opt = photo.display
        photo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20150210_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='display_opt',
            field=imagekit.models.fields.ProcessedImageField(default=' ', upload_to=app.models.upload_optimized),
            preserve_default=False,
        ),
        migrations.RunPython(processImages),

    ]
