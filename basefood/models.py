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
    categorymain = models.ManyToManyField('CategoryMain')
    parent = models.ForeignKey('Category', blank=True, null=True)

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
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField()
    image2 = models.ImageField()
    category = models.ManyToManyField('Category')
    categorymain = models.ManyToManyField('CategoryMain')
    sugar = models.FloatField()
    size = models.FloatField()
    protein = models.FloatField()
    vitamins = models.ManyToManyField('Vitamin')
    minerals = models.ManyToManyField('Mineral')
    carbohydrates = models.FloatField()
    fats = models.FloatField()
    fatsSaturated = models.FloatField()
    energyValue = models.FloatField()
    portion = models.FloatField()
    preservatives = models.ManyToManyField('Preservative')
    shops = models.ManyToManyField('Shop')
    pricemin = models.FloatField()
    pricemax = models.FloatField()

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __unicode__(self):
        return "%s" % self.name