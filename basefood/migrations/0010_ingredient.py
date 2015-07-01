# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0009_auto_20150622_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('allergen', models.BooleanField()),
                ('gluten', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Sk\u0142adnik',
                'verbose_name_plural': 'Sk\u0142adniki',
            },
            bases=(models.Model,),
        ),
    ]
