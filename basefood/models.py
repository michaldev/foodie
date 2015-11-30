# -*- coding: utf-8 -*-
from urllib2 import URLError

from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from geopy.geocoders.google import Google
from geopy.geocoders.google import GQueryError


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
    othername = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255, blank=True)

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
    description = models.CharField(max_length=255, blank=True)

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
    othername = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255, blank=True)
    #level = models.IntegerField(default=0, blank=True)
    dmax = models.FloatField(default=0, blank=True)  # dopuszczalna dzienna dawka

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
    image = models.ImageField(blank=True)
    shop = models.ManyToManyField('Shop')
    location = gis_models.PointField(u"longitude/latitude",
                                     geography=True, blank=True, null=True)
    gis = gis_models.GeoManager()
    objects = models.Manager()

    class Meta:
        verbose_name = "Lokalizacja sklepu"
        verbose_name_plural = "Lokalizacja sklepów"

    def __unicode__(self):
        return "%s" % self.slug

    def save(self, **kwargs):
        if not self.location:
            address = u'%s %s' % (self.city, self.address)
            address = address.encode('utf-8')
            geocoder = Google()
            try:
                _, latlon = geocoder.geocode(address)
            except (URLError, GQueryError, ValueError):
                pass
            else:
                point = "POINT(%s %s)" % (latlon[1], latlon[0])
                self.location = geos.fromstr(point)
        super(ShopLocal, self).save()


class Shop(models.Model):
    """
    Shop model
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(blank=True)

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
    producer = models.ManyToManyField('Producer', verbose_name="Producenci", blank=True)
    slug = models.SlugField(verbose_name='Adres', unique=True, blank=True)
    image = models.ImageField(verbose_name='Zdjęcie produktu', blank=True)
    image2 = models.ImageField(verbose_name='Zdjęcie etykiety', blank=True)
    category = models.ManyToManyField('Category', verbose_name='Kategoria', blank=True)
    sugar = models.FloatField(verbose_name='Cukier na 100g/ml', blank=True)
    size = models.FloatField(verbose_name='Waga/Objętość', blank=True)
    protein = models.FloatField(verbose_name='Białko na 100g/ml', blank=True)
    vitamins = models.ManyToManyField('Vitamin', verbose_name='Witaminy', blank=True)
    minerals = models.ManyToManyField('Mineral', verbose_name='Minerały', blank=True)
    ingredients = models.ManyToManyField(
        'Ingredient', verbose_name='Składniki', blank=True)
    carbohydrates = models.FloatField(verbose_name='Węglowodany', blank=True)
    fats = models.FloatField(verbose_name='Tłuszcze', blank=True)
    fatsSaturated = models.FloatField(verbose_name='Tłuszcze nasycone', blank=True)
    energyValue = models.FloatField(verbose_name='Wartość energetyczna', blank=True)
    portion = models.FloatField(verbose_name='Porcja', blank=True)
    preservatives = models.ManyToManyField(
        'Preservative', verbose_name='Konserwanty', blank=True)
    shops = models.ManyToManyField(
        'Shop', verbose_name='Sklepy', blank=True)
    barcode = models.IntegerField(blank=True)

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __unicode__(self):
        return "%s" % self.name


class Contact(models.Model):
    """
    contact model
    """
    type = models.IntegerField()
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1024)
    mail = models.EmailField()

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickety"

    def __unicode__(self):
        return "%s" % self.title