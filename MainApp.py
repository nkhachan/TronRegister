import kivy

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel


class TransactionPage:
    def __init__(self):
        self.text = "Fuck me"


class MainLayout(TabbedPanel):
    def __init__(self):
        self.page = TransactionPage()

class MainApp(App):

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

    def build(self):
        layout = MainLayout()
        return layout

