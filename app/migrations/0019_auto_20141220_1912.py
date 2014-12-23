# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20141220_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='hardscape',
            fields=[
                ('photogroup_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.photogroup')),
                ('architecture', models.CharField(default=b'L', max_length=1, choices=[(b'L', b'LandScapes'), (b'H', b'HardScapes')])),
            ],
            options={
            },
            bases=('app.photogroup',),
        ),
        migrations.CreateModel(
            name='landscape',
            fields=[
                ('photogroup_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.photogroup')),
                ('architecture', models.CharField(default=b'L', max_length=1, choices=[(b'L', b'LandScapes'), (b'H', b'HardScapes')])),
            ],
            options={
            },
            bases=('app.photogroup',),
        ),
        migrations.RemoveField(
            model_name='hardscapes',
            name='photogroup_ptr',
        ),
        migrations.DeleteModel(
            name='hardscapes',
        ),
        migrations.RemoveField(
            model_name='landscapes',
            name='photogroup_ptr',
        ),
        migrations.DeleteModel(
            name='landscapes',
        ),
    ]
