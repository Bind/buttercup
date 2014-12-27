# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20141227_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='full_pdf',
            field=models.FileField(null=True, upload_to=app.models.upload_to_media, blank=True),
            preserve_default=True,
        ),
    ]
