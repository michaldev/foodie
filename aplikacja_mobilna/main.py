from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.event import EventDispatcher

from kivy.properties import StringProperty


class HelloApp(App):
    pass


class GlownyElement(BoxLayout):
    pass


class Taby(TabbedPanel):
    pass


class Stopka(BoxLayout):
    pass


class Widok(BoxLayout):
    def __init__(self, **kwargs):
        super(Widok, self).__init__(**kwargs)
        for i in range(10):
            w = Wynik(name='aaa', producer='s')
            self.add_widget(w)


class Wynik(BoxLayout):
    name = StringProperty('')
    producer = StringProperty('')


class Widok2(BoxLayout):
    pass


if __name__ == '__main__':
    HelloApp().run()
