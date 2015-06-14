# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0002_price_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pricemax',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pricemin',
        ),
    ]
