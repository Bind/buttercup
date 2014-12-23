# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_photo_splash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.ForeignKey(related_name='pictures', blank=True, to='app.location', null=True),
            preserve_default=True,
        ),
    ]
