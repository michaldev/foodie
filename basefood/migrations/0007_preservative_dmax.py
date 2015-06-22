# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0006_auto_20150621_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='preservative',
            name='dmax',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
