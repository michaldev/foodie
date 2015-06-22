# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0008_shoplocal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoplocal',
            name='address',
            field=models.CharField(max_length=100, verbose_name=b'Adres'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shoplocal',
            name='city',
            field=models.CharField(max_length=50, verbose_name=b'Miasto'),
            preserve_default=True,
        ),
    ]
