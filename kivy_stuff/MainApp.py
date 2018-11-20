from LoginPage import *
from MainPage import MainPage
from kivy.config import Config
from kivy.app import App

class MainApp(App):

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

    def build(self):

        Config.set('graphics', 'width', '1500')
        Config.set('graphics', 'height', '1000')
        return MainPage()

