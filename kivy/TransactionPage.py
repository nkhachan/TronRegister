from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MainPage(GridLayout):

    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Button(text='Hello 1'))
        self.add_widget(Button(text='World 1'))
        self.add_widget(Label   (text='Hello 2'))
        self.add_widget(Label(text='Wrld 2'))