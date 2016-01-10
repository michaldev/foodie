# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preservative',
            name='level',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='portion',
            field=models.FloatField(null=True, verbose_name=b'Porcja', blank=True),
        ),
    ]
