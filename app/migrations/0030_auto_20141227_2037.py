# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20141227_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='website',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='url',
            field=models.URLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
