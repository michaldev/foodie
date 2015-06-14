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
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Minera\u0142',
                'verbose_name_plural': 'Minera\u0142y',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Preservative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('othername', models.CharField(default=b'', max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(max_length=255)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Konserwant',
                'verbose_name_plural': 'Konserwanty',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_change', models.DateField()),
            ],
            options={
                'verbose_name': 'Cena',
                'verbose_name_plural': 'Ceny',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nazwa')),
                ('producer', models.CharField(max_length=255, verbose_name=b'Producent')),
                ('slug', models.SlugField(unique=True, verbose_name=b'Adres')),
                ('image', models.ImageField(upload_to=b'', verbose_name=b'Zdj\xc4\x99cie produktu')),
                ('image2', models.ImageField(upload_to=b'', verbose_name=b'Zdj\xc4\x99cie etykiety')),
                ('sugar', models.FloatField(verbose_name=b'Cukier na 100g/ml')),
                ('size', models.FloatField(verbose_name=b'Waga/Obj\xc4\x99to\xc5\x9b\xc4\x87')),
                ('protein', models.FloatField(verbose_name=b'Bia\xc5\x82ko na 100g/ml')),
                ('carbohydrates', models.FloatField(verbose_name=b'W\xc4\x99glowodany')),
                ('fats', models.FloatField(verbose_name=b'T\xc5\x82uszcze')),
                ('fatsSaturated', models.FloatField(verbose_name=b'T\xc5\x82uszcze nasycone')),
                ('energyValue', models.FloatField(verbose_name=b'Warto\xc5\x9b\xc4\x87 energetyczna')),
                ('portion', models.FloatField(verbose_name=b'Porcja')),
                ('pricemin', models.FloatField(verbose_name=b'Cena min')),
                ('pricemax', models.FloatField(verbose_name=b'Cena max')),
                ('category', models.ManyToManyField(to='basefood.Category', verbose_name=b'Kategoria')),
                ('minerals', models.ManyToManyField(to='basefood.Mineral', verbose_name=b'Minera\xc5\x82y')),
                ('preservatives', models.ManyToManyField(to='basefood.Preservative', verbose_name=b'Konserwanty')),
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
                ('othername', models.CharField(default=b'', max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(max_length=255)),
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
            field=models.ManyToManyField(to='basefood.Shop', verbose_name=b'Sklepy', through='basefood.Price'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='vitamins',
            field=models.ManyToManyField(to='basefood.Vitamin', verbose_name=b'Witaminy'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(to='basefood.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='price',
            name='shop',
            field=models.ForeignKey(to='basefood.Shop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='categorymain',
            field=models.ManyToManyField(to='basefood.CategoryMain', verbose_name=b'G\xc5\x82\xc3\xb3wna kategoria'),
            preserve_default=True,
        ),
    ]
