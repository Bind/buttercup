# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20141220_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='hardscape',
            field=models.ForeignKey(related_name='pictures', blank=True, to='app.hardscape', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='landscape',
            field=models.ForeignKey(related_name='pictures', blank=True, to='app.landscape', null=True),
            preserve_default=True,
        ),
    ]
