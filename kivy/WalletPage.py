import sys
import os
sys.path.append(os.getcwd() + "/../src")
from User import user
from TronAPI import getformattedBalance

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.clock import Clock


Builder.load_string("""
<AddressDisplay>
    canvas.before:
        Color:
            rgba: 0, 46, 140, 0.6
        Rectangle:
            pos: self.pos
            size: self.size

<BalanceDisplay>
    canvas.before:
        Color:
            rgba: 119, 8, 42, 0.78
        Rectangle:
            pos: self.pos
            size: self.size

<BlocksDisplay>
    canvas.before:
        Color:
            rgba: 1, .5, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

""")


class AddressDisplay(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=2, size_hint_y = 0.15)
        self.add_widget(Label(text=user.address, font_size="40px"))


class BalanceDisplay(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=2, rows=1, size_hint_y = 0.20)
        self.balance = Label(text='SomeNumber', font_size="40px")
        self.add_widget(self.balance)
        Clock.schedule_interval(self.getBalance, 1)

    def getBalance(self, dt):
        newbalance = getformattedBalance(user.address)
        self.balance.text = str(newbalance)

class BlocksDisplay(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=2, rows=1)
        self.add_widget(Label(text='Stuff3'))
        self.add_widget(Label(text='Stuff4'))

class BalanceBlocksDisplay(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=2)
        self.add_widget(BalanceDisplay())
        self.add_widget(BlocksDisplay())


class WalletPage(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=2)
        self.add_widget(AddressDisplay())
        self.add_widget(BalanceBlocksDisplay())
