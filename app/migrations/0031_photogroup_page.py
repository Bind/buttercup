# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20141227_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='photogroup',
            name='page',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
