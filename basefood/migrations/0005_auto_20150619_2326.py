# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0004_auto_20150619_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='product',
            field=models.ForeignKey(related_name='ppp', verbose_name=b'Produkt', to='basefood.Product'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='price',
            name='shop',
            field=models.ForeignKey(related_name='sss', verbose_name=b'Sklep', to='basefood.Shop'),
            preserve_default=True,
        ),
    ]
