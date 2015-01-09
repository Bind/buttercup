# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_photogroup_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photogroup',
            name='page',
        ),
        migrations.AddField(
            model_name='photogroup',
            name='order',
            field=models.PositiveIntegerField(default=1, max_length=4),
            preserve_default=True,
        ),
    ]
