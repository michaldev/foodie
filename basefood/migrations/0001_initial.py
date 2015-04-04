# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryMain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'G\u0142\xf3wna Kategoria',
                'verbose_name_plural': 'G\u0142\xf3wne Kategorie',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Konserwant',
                'verbose_name_plural': 'Produkty',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Preservative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Konserwant',
                'verbose_name_plural': 'Konserwanty',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('image2', models.ImageField(upload_to=b'')),
                ('sugar', models.FloatField()),
                ('size', models.FloatField()),
                ('protein', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('fats', models.FloatField()),
                ('fatsSaturated', models.FloatField()),
                ('energyValue', models.FloatField()),
                ('portion', models.FloatField()),
                ('pricemin', models.FloatField()),
                ('pricemax', models.FloatField()),
                ('category', models.ManyToManyField(to='basefood.Category')),
                ('categorymain', models.ManyToManyField(to='basefood.CategoryMain')),
                ('minerals', models.ManyToManyField(to='basefood.Mineral')),
                ('preservatives', models.ManyToManyField(to='basefood.Preservative')),
            ],
            options={
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkty',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to=b'')),
            ],
            options={
                'verbose_name': 'Sklep',
                'verbose_name_plural': 'Sklepy',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vitamin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Witamina',
                'verbose_name_plural': 'Witaminy',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='shops',
            field=models.ManyToManyField(to='basefood.Shop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='vitamins',
            field=models.ManyToManyField(to='basefood.Vitamin'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='categorymain',
            field=models.ManyToManyField(to='basefood.CategoryMain'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, to='basefood.Category', null=True),
            preserve_default=True,
        ),
    ]
