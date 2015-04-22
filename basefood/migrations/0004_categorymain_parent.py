# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0003_auto_20150422_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymain',
            name='parent',
            field=models.ForeignKey(blank=True, to='basefood.CategoryMain', null=True),
            preserve_default=True,
        ),
    ]
