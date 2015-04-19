# -*- coding: utf-8 -*-
from django.db import models


class CategoryMain(models.Model):
    """
    Main Category
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    #parent = models.ForeignKey('CategoryMain', blank=True, null=True)

    class Meta:
        verbose_name = "Główna Kategoria"
        verbose_name_plural = "Główne Kategorie"

    def __unicode__(self):
        return "%s" % self.name


class Category(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    categorymain = models.ManyToManyField('CategoryMain', 
        verbose_name='Główna kategoria')
    #parent = models.ForeignKey('Category', blank=True, null=True)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __unicode__(self):
        return "%s" % self.name


class Vitamin(models.Model):
    """
    Vitamin model
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Witamina"
        verbose_name_plural = "Witaminy"

    def __unicode__(self):
        return "%s" % self.name


class Mineral(models.Model):
    """
    Mineral model
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Konserwant"
        verbose_name_plural = "Produkty"

    def __unicode__(self):
        return "%s" % self.name


class Preservative(models.Model):
    """
    Preservative model
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Konserwant"
        verbose_name_plural = "Konserwanty"

    def __unicode__(self):
        return "%s" % self.name


class Shop(models.Model):
    """
    Shop model
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField()

    class Meta:
        verbose_name = "Sklep"
        verbose_name_plural = "Sklepy"

    def __unicode__(self):
        return "%s" % self.name


class Product(models.Model):
    """
    Product model
    """
    name = models.CharField(verbose_name='Nazwa', max_length=255)
    producer = models.CharField(verbose_name='Producent', max_length=255)
    slug = models.SlugField(verbose_name='Adres', unique=True)
    image = models.ImageField(verbose_name='Zdjęcie produktu')
    image2 = models.ImageField(verbose_name='Zdjęcie etykiety')
    category = models.ManyToManyField('Category', verbose_name='Kategoria')
    sugar = models.FloatField(verbose_name='Cukier na 100g/ml')
    size = models.FloatField(verbose_name='Waga/Objętość')
    protein = models.FloatField(verbose_name='Białko na 100g/ml')
    vitamins = models.ManyToManyField('Vitamin', verbose_name='Witaminy')
    minerals = models.ManyToManyField('Mineral', verbose_name='Minerały')
    carbohydrates = models.FloatField(verbose_name='Węglowodany')
    fats = models.FloatField(verbose_name='Tłuszcze')
    fatsSaturated = models.FloatField(verbose_name='Tłuszcze nasycone')
    energyValue = models.FloatField(verbose_name='Wartość energetyczna')
    portion = models.FloatField(verbose_name='Porcja')
    preservatives = models.ManyToManyField('Preservative', verbose_name='Konserwanty')
    shops = models.ManyToManyField('Shop', verbose_name='Sklepy')
    pricemin = models.FloatField(verbose_name='Cena min')
    pricemax = models.FloatField(verbose_name='Cena max')

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __unicode__(self):
        return "%s" % self.name