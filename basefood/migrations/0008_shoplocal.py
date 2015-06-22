# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0007_preservative_dmax'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopLocal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'Lokalizacja sklepu',
                'verbose_name_plural': 'Lokalizacja sklep\xf3w',
            },
            bases=(models.Model,),
        ),
    ]
