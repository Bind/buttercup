# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141116_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='display',
            field=models.ImageField(null=True, upload_to=app.models.upload_to_s3, blank=True),
            preserve_default=True,
        ),
    ]
