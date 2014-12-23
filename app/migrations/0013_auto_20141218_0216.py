# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20141122_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='detail',
            field=models.CharField(max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='detail',
            field=models.CharField(max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
    ]
