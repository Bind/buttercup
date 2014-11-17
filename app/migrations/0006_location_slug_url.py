# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_photo_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='slug_url',
            field=models.SlugField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
