# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0010_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(to='basefood.Ingredient', verbose_name=b'Sk\xc5\x82adniki'),
            preserve_default=True,
        ),
    ]
