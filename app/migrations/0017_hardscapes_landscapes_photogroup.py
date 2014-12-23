# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20141220_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='photogroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('slug_url', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=[b'name'], blank=True, null=True, overwrite=True)),
                ('detail', models.CharField(max_length=512, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='landscapes',
            fields=[
                ('photogroup_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.photogroup')),
                ('architecture', models.CharField(default=b'L', max_length=1, choices=[(b'L', b'LandScapes'), (b'H', b'HardScapes')])),
            ],
            options={
            },
            bases=('app.photogroup',),
        ),
        migrations.CreateModel(
            name='hardscapes',
            fields=[
                ('photogroup_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.photogroup')),
                ('architecture', models.CharField(default=b'L', max_length=1, choices=[(b'L', b'LandScapes'), (b'H', b'HardScapes')])),
            ],
            options={
            },
            bases=('app.photogroup',),
        ),
    ]
