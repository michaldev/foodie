# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0004_categorymain_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, to='basefood.Category', null=True),
            preserve_default=True,
        ),
    ]
