# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models
import imagekit.models.fields

from imagekit import ImageSpec
from imagekit.processors import ResizeToFill

class LandScapeThumbnail(ImageSpec):
    processsors = [ResizeToFill(1200,900)]
    format = 'JPEG'
    options = { 'quality':60 }

class PortaitThumbnail(ImageSpec):
    processsors = [ResizeToFill(900,1200)]
    format = 'JPEG'
    options = { 'quality':60 }    



def createThumbnails(apps,schema_editor):
    photo = apps.get_model("app","photo")
    for p in photo.objects.all():
        if p.height > p.width:
            p.thumbnail = PortaitThumbnail(source=p.display)
            print "portrait"
        else:
            print ""
            p.thumbnail = LandScapeThumbnail(source=p.display)
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20150212_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=app.models.upload_optimized, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='display',
            field=imagekit.models.fields.ProcessedImageField(height_field=b'height', width_field=b'width', null=True, upload_to=app.models.upload_to_s3, blank=True),
            preserve_default=True,
        ),
    ]
