#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, urllib2
import gtk

class ProductInfo:
    slug = "jogobella"
    data = urllib2.urlopen("http://melonlab.pl/basefood/products?slug="+slug)
    json_data = json.loads(data.read())
    json_data = json_data[0]
    
    def get_data(self):
        return self.json_data
        
    def get_name(self):
        return self.json_data["name"]
        
    def get_producer(self):
        return self.json_data["producer"]
        
    def get_image(self):
        return self.json_data["image"]
        
    def get_sugar(self):
        return self.json_data["sugar"]
        
    def get_category(self):
        return self.json_data["category"][0]["name"]
        
    def get_protein(self):
        return self.json_data["protein"]
        
    def get_fat(self):
		return self.json_data["fats"]
            
            
            
class SearchProduct:
    key = "jogo"
    data = urllib2.urlopen("http://melonlab.pl/basefood/productsearch?search="+key)
    json_data = json.loads(data.read())
    def get_data(self):
        return self.json_data
    

class MainWindow:
    product = ProductInfo()
    def destroy(self, widget):
        gtk.main_quit()
        
    def __init__(self):
        self.window = gtk.Window()
        self.window.set_title("Foodie - "+self.product.get_name()+" - "+self.product.get_producer())
        self.window.set_size_request(400, 500)
        self.window.connect("destroy", self.destroy)
        self.fixed = gtk.Fixed()
        self.image = gtk.Image()
        self.sugar = gtk.Label()
        self.category = gtk.Label()
        self.name = gtk.Label()
        self.progressbarSugar = gtk.ProgressBar(adjustment=None)
        self.progressbarSugar.set_fraction(0.2)
        self.protein = gtk.Label()
        self.fat = gtk.Label()
        self.progressbarProtein = gtk.ProgressBar(adjustment=None)
        self.progressbarProtein.set_fraction(0.3)
        self.progressbarFat = gtk.ProgressBar(adjustment=None)
        self.progressbarFat.set_fraction(0.1)
        loader = gtk.gdk.PixbufLoader()
        loader.write(urllib2.urlopen(self.product.get_image()).read())
        loader.close()
        self.image.set_from_pixbuf(loader.get_pixbuf().scale_simple(200,200,gtk.gdk.INTERP_BILINEAR))
        self.sugar.set_markup("<b>Cukier:</b> "+str(self.product.get_sugar()))
        self.protein.set_markup("<b>Białko:</b> "+str(self.product.get_protein()))
        self.fat.set_markup("<b>Tłuszcz:</b> "+str(self.product.get_fat()))
        self.name.set_markup("<span size='x-large'>"+self.product.get_name()+" - "+self.product.get_producer()+"</span>")
        self.category.set_markup("<b>Kategoria:</b> "+str(self.product.get_category()))
        self.fixed.put(self.image,1 ,1)
        self.fixed.put(self.sugar, 250, 20)
        self.fixed.put(self.progressbarSugar, 225, 40)
        self.fixed.put(self.protein, 250, 70)
        self.fixed.put(self.progressbarProtein, 225, 90)
        self.fixed.put(self.fat, 250, 120)
        self.fixed.put(self.progressbarFat, 225, 140)
        self.fixed.put(self.name, 10, 220)
        self.fixed.put(self.category, 10, 250)
        self.window.add(self.fixed)
        self.window.show_all()


if __name__=="__main__":
    MainWindow()
    gtk.main()
