# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20141220_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='display',
            new_name='cover_image',
        ),
        migrations.AddField(
            model_name='media',
            name='full_pdf',
            field=models.ImageField(null=True, upload_to=app.models.upload_to_media, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='slug_url',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=[b'name', b'display'], blank=True, null=True, overwrite=True),
            preserve_default=True,
        ),
    ]
