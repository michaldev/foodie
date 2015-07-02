# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefood', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producer',
            old_name='poland_producer',
            new_name='local_producer',
        ),
    ]
