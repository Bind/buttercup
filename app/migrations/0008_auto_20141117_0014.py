# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20141117_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='slug_url',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=[b'name'], blank=True, null=True, overwrite=True),
            preserve_default=True,
        ),
    ]
