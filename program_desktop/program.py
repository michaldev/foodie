#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, urllib2
import gtk

class ProductInfo:
    slug = "jogobella"
    data = urllib2.urlopen("http://melonlab.pl/basefood/products?slug="+slug)
    json_data = json.loads(data.read())
    json_data = json_data[0]
    def show_data(self):
        return self.json_data
    def show_name(self):
        return self.json_data["name"]
    def show_producer(self):
        return self.json_data["producer"]
    def show_image(self):
        return self.json_data["image"]
    def show_sugar(self):
        return self.json_data["sugar"]
    def show_category(self):
		return self.json_data["category"][0]["name"]
        
class SearchProduct:
    key = "jogo"
    data = urllib2.urlopen("http://melonlab.pl/basefood/productsearch?search="+key)
    json_data = json.loads(data.read())
    def show_data(self):
        return self.json_data
    

class MainWindow:
    product = ProductInfo()
    def destroy(self, widget):
        gtk.main_quit()
        
    def __init__(self):
        self.window = gtk.Window()
        self.window.set_title("Foodie - "+self.product.show_name()+" "+self.product.show_producer())
        self.window.set_size_request(400, 500)
        self.window.connect("destroy", self.destroy)
        self.fixed = gtk.Fixed()
        self.image = gtk.Image()
        self.sugar = gtk.Label()
        self.category = gtk.Label()
        loader = gtk.gdk.PixbufLoader()
        loader.write(urllib2.urlopen(self.product.show_image()).read())
        loader.close()
        self.image.set_from_pixbuf(loader.get_pixbuf().scale_simple(200,200,gtk.gdk.INTERP_BILINEAR))
        self.sugar.set_markup("<b>Sugar:</b> "+str(self.product.show_sugar()))
        self.category.set_markup("<b>Kategoria:</b> "+str(self.product.show_category()))
        self.fixed.put(self.image,1 ,1)
        self.fixed.put(self.sugar, 220, 20)
        self.fixed.put(self.category, 10, 220)
        self.window.add(self.fixed)
        self.window.show_all()


if __name__=="__main__":
    MainWindow()
    gtk.main()
