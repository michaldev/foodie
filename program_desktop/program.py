#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, urllib2
import gtk

class MainWindow():
	def load_data():
		data = urllib2.urlopen("http://melonlab.pl/basefood/products?slug=jogobella")
		json_data = json.loads(data.read())
    def __init__(self):
        self.window = gtk.Window()
        self.window.set_title("Foodie - Logowanie")
        self.window.set_size_request(400, 500)
        self.fixed = gtk.Fixed()
        self.image = gtk.Image()
        loader = gtk.gdk.PixbufLoader()
        loader.write(urllib2.urlopen().read())
        loader.close()
        self.image.set_from_pixbuf(loader.get_pixbuf())
        self.fixed.put(self.image,1 ,1)
        self.window.add(self.fixed)
        self.window.show_all()


if __name__=="__main__":
    MainWindow()
    gtk.main()
