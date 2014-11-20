# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_media'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='photo',
            name='Splash',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'L', b'LandScapes'), (b'H', b'HardScapes')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='display',
            field=models.ImageField(null=True, upload_to=app.models.upload_to_media, blank=True),
            preserve_default=True,
        ),
    ]
