# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20141218_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='rollover',
        ),
        migrations.AddField(
            model_name='photo',
            name='hero',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
