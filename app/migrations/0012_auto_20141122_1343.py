# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20141120_0228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default='_', max_length=255),
            preserve_default=False,
        ),
    ]
