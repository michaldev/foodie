# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0005_auto_20150619_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='product',
            field=models.ForeignKey(verbose_name=b'Produkt', to='basefood.Product'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='price',
            name='shop',
            field=models.ForeignKey(verbose_name=b'Sklep', to='basefood.Shop'),
            preserve_default=True,
        ),
    ]
