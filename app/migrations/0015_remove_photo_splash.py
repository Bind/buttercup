# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20141218_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='Splash',
        ),
    ]
