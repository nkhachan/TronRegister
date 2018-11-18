from kivy.graphics import Color, Rectangle
from LoginPage import *
from TransactionPage import MainPage

class MainApp(App):

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

    def build(self):
        return MainPage()

