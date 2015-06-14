# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='price',
            field=models.FloatField(default=0, verbose_name=b'Cena'),
            preserve_default=True,
        ),
    ]
