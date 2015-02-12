# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20150212_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='photo',
            name='display',
            field=imagekit.models.fields.ProcessedImageField(height_field=b'height', width_field=b'width', null=True, upload_to=app.models.upload_optimized, blank=True),
            preserve_default=True,
        ),
    ]
