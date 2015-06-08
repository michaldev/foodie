# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0005_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='categorymain',
            name='parent',
        ),
        migrations.AddField(
            model_name='preservative',
            name='othername',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vitamin',
            name='othername',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
