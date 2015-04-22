# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0002_preservative_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mineral',
            options={'verbose_name': 'Minera\u0142', 'verbose_name_plural': 'Minera\u0142y'},
        ),
        migrations.AlterField(
            model_name='preservative',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
