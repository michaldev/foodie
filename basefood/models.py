# -*- coding: utf-8 -*-
from django.db import models


class CategoryMain(models.Model):
    """
    Main Category
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

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
    categorymain = models.ManyToManyField(
        'CategoryMain', verbose_name='Główna kategoria')

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
    othername = models.CharField(max_length=255, default="")
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
        verbose_name = "Minerał"
        verbose_name_plural = "Minerały"

    def __unicode__(self):
        return "%s" % self.name


class Preservative(models.Model):
    """
    Preservative model
    """
    name = models.CharField(max_length=255)
    othername = models.CharField(max_length=255, default="")
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255)
    level = models.IntegerField(default=0)
    dmax = models.FloatField(default=0)  # dopuszczalna dzienna dawka

    class Meta:
        verbose_name = "Konserwant"
        verbose_name_plural = "Konserwanty"

    def __unicode__(self):
        return "%s" % self.name


class ShopLocal(models.Model):
    """
    Shoplocal model
    """
    address = models.CharField(max_length=100, verbose_name="Adres")
    city = models.CharField(max_length=50, verbose_name="Miasto")
    slug = models.SlugField(unique=True)
    image = models.ImageField()
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Lokalizacja sklepu"
        verbose_name_plural = "Lokalizacja sklepów"

    def __unicode__(self):
        return "%s" % self.slug


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


class Producer(models.Model):
    """
    Producer model
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    #image = models.ImageField()
    local_producer = models.BooleanField(default=None)

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"

    def __unicode__(self):
        return "%s" % self.name


class Price(models.Model):
    price = models.FloatField(verbose_name="Cena", default=0)
    product = models.ForeignKey("Product", verbose_name="Produkt")
    shop = models.ForeignKey("Shop", verbose_name="Sklep")
    date_change = models.DateField(verbose_name="Data modyfikacji")

    class Meta:
        verbose_name = "Cena"
        verbose_name_plural = "Ceny"

    def __unicode__(self):
        return "%s" % self.product


class Ingredient(models.Model):
    """
    ingredient model
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    #image = models.ImageField()
    allergen = models.BooleanField(default=None)
    gluten = models.BooleanField(default=None)

    class Meta:
        verbose_name = "Składnik"
        verbose_name_plural = "Składniki"

    def __unicode__(self):
        return "%s" % self.name


class Product(models.Model):
    """
    Product model
    """
    name = models.CharField(verbose_name='Nazwa', max_length=255)
    producer = models.ManyToManyField('Producer', verbose_name="Producenci")
    slug = models.SlugField(verbose_name='Adres', unique=True)
    image = models.ImageField(verbose_name='Zdjęcie produktu')
    image2 = models.ImageField(verbose_name='Zdjęcie etykiety')
    category = models.ManyToManyField('Category', verbose_name='Kategoria')
    sugar = models.FloatField(verbose_name='Cukier na 100g/ml')
    size = models.FloatField(verbose_name='Waga/Objętość')
    protein = models.FloatField(verbose_name='Białko na 100g/ml')
    vitamins = models.ManyToManyField('Vitamin', verbose_name='Witaminy')
    minerals = models.ManyToManyField('Mineral', verbose_name='Minerały')
    ingredients = models.ManyToManyField(
        'Ingredient', verbose_name='Składniki')
    carbohydrates = models.FloatField(verbose_name='Węglowodany')
    fats = models.FloatField(verbose_name='Tłuszcze')
    fatsSaturated = models.FloatField(verbose_name='Tłuszcze nasycone')
    energyValue = models.FloatField(verbose_name='Wartość energetyczna')
    portion = models.FloatField(verbose_name='Porcja')
    preservatives = models.ManyToManyField(
        'Preservative', verbose_name='Konserwanty')
    shops = models.ManyToManyField(
        'Shop', verbose_name='Sklepy', through="Price")

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __unicode__(self):
        return "%s" % self.name
