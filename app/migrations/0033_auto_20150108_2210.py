# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20150108_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photogroup',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='photo',
            name='height',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='width',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='display',
            field=models.ImageField(height_field=b'height', width_field=b'width', null=True, upload_to=app.models.upload_to_s3, blank=True),
            preserve_default=True,
        ),
    ]
