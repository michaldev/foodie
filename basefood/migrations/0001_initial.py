# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


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
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField()),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=1024)),
                ('mail', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickety',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('allergen', models.BooleanField(default=None)),
                ('gluten', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name': 'Sk\u0142adnik',
                'verbose_name_plural': 'Sk\u0142adniki',
            },
        ),
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'Minera\u0142',
                'verbose_name_plural': 'Minera\u0142y',
            },
        ),
        migrations.CreateModel(
            name='Preservative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('othername', models.CharField(max_length=255, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('dmax', models.FloatField(default=0, blank=True)),
            ],
            options={
                'verbose_name': 'Konserwant',
                'verbose_name_plural': 'Konserwanty',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('local_producer', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name': 'Producent',
                'verbose_name_plural': 'Producenci',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nazwa')),
                ('slug', models.SlugField(unique=True, verbose_name=b'Adres', blank=True)),
                ('image', models.ImageField(upload_to=b'', verbose_name=b'Zdj\xc4\x99cie produktu', blank=True)),
                ('image2', models.ImageField(upload_to=b'', verbose_name=b'Zdj\xc4\x99cie etykiety', blank=True)),
                ('sugar', models.FloatField(null=True, verbose_name=b'Cukier na 100g/ml')),
                ('size', models.FloatField(null=True, verbose_name=b'Waga/Obj\xc4\x99to\xc5\x9b\xc4\x87')),
                ('protein', models.FloatField(null=True, verbose_name=b'Bia\xc5\x82ko na 100g/ml')),
                ('carbohydrates', models.FloatField(null=True, verbose_name=b'W\xc4\x99glowodany')),
                ('fats', models.FloatField(null=True, verbose_name=b'T\xc5\x82uszcze')),
                ('fatsSaturated', models.FloatField(null=True, verbose_name=b'T\xc5\x82uszcze nasycone')),
                ('energyValue', models.FloatField(null=True, verbose_name=b'Warto\xc5\x9b\xc4\x87 energetyczna')),
                ('portion', models.FloatField(null=True, verbose_name=b'Porcja')),
                ('barcode', models.IntegerField(null=True)),
                ('category', models.ManyToManyField(to='basefood.Category', verbose_name=b'Kategoria', blank=True)),
                ('ingredients', models.ManyToManyField(to='basefood.Ingredient', verbose_name=b'Sk\xc5\x82adniki', blank=True)),
                ('minerals', models.ManyToManyField(to='basefood.Mineral', verbose_name=b'Minera\xc5\x82y', blank=True)),
                ('preservatives', models.ManyToManyField(to='basefood.Preservative', verbose_name=b'Konserwanty', blank=True)),
                ('producer', models.ForeignKey(verbose_name=b'Producenci', to='basefood.Producer')),
            ],
            options={
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkty',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to=b'', blank=True)),
            ],
            options={
                'verbose_name': 'Sklep',
                'verbose_name_plural': 'Sklepy',
            },
        ),
        migrations.CreateModel(
            name='ShopLocal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=100, verbose_name=b'Adres')),
                ('city', models.CharField(max_length=50, verbose_name=b'Miasto')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to=b'', blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True, null=True, verbose_name='longitude/latitude', blank=True)),
                ('shop', models.ManyToManyField(to='basefood.Shop', blank=True)),
            ],
            options={
                'verbose_name': 'Lokalizacja sklepu',
                'verbose_name_plural': 'Lokalizacja sklep\xf3w',
            },
        ),
        migrations.CreateModel(
            name='Vitamin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('othername', models.CharField(max_length=255, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'Witamina',
                'verbose_name_plural': 'Witaminy',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='shops',
            field=models.ManyToManyField(to='basefood.Shop', verbose_name=b'Sklepy', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='vitamins',
            field=models.ManyToManyField(to='basefood.Vitamin', verbose_name=b'Witaminy', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='categorymain',
            field=models.ManyToManyField(to='basefood.CategoryMain', verbose_name=b'G\xc5\x82\xc3\xb3wna kategoria'),
        ),
    ]
