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
        
class SearchProduct:
    key = "jogo"
    data = urllib2.urlopen("http://melonlab.pl/basefood/productsearch?search="+key)
    json_data = json.loads(data.read())
    def show_data(self):
        return self.json_data
    

class MainWindow():
    def destroy(self, widget):
        gtk.main_quit()
        
    def __init__(self):
        self.window = gtk.Window()
        self.window.set_title("Foodie - Logowanie")
        self.window.set_size_request(400, 500)
        self.window.connect("destroy", self.destroy)
        self.fixed = gtk.Fixed()
        self.image = gtk.Image()
        #loader = gtk.gdk.PixbufLoader()
        #loader.write(urllib2.urlopen().read())
        #loader.close()
        #self.image.set_from_pixbuf(loader.get_pixbuf())
        self.fixed.put(self.image,1 ,1)
        self.window.add(self.fixed)
        self.window.show_all()


if __name__=="__main__":
    produkt = ProductInfo()
    print produkt.show_name()
    MainWindow()
    gtk.main()
