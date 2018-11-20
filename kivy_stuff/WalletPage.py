import sys
import os
sys.path.append(os.getcwd() + "/../src")
from User import user
from TronAPI import getformattedBalance
from Binance import getTRXtoUSD

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
#from kivy.clock import Clock

SPACING = 25


Builder.load_string("""
<AddressDisplay>
    padding: 20
    canvas.before:
        Color:
            rgb: 0.19, 0.19, 0.19
        Rectangle:
            pos: self.pos
            size: self.size

<MidDisplay>
    canvas.before:
        Color:
            rgb: 0.14, 0.14, 0.14
        Rectangle:
            pos: self.pos
            size: self.size

<BlocksDisplay>
    canvas.before:
        Color:
            rgb: 0.14, 0.14, 0.14
        Rectangle:
            pos: self.pos
            size: self.size
            
            
<ToAddressBlocks>
    canvas.before:
        Color:
            rgb: 0.19, 0.19, 0.19
        Rectangle:
            pos: self.pos
            size: self.size
            
<FromAddressBlocks>
    canvas.before:
        Color:
            rgb: 0.19, 0.19, 0.19
        Rectangle:
            pos: self.pos
            size: self.size
            
<WalletPage>
    canvas.before:
        Color:
            rgb: 0.14, 0.14, 0.14
        Rectangle:
            pos: self.pos
            size: self.size

<BalanceDisplay>
    canvas.before:
        Color:
            rgb: 0.19, 0.19, 0.19
        Rectangle:
            pos: self.pos
            size: self.size
            
<TronPowerDisplay>
    canvas.before:
        Color:
            rgb: 0.19, 0.19, 0.19
        Rectangle:
            pos: self.pos
            size: self.size
            
<ConversionDisplay>
    canvas.before:
        Color:
            rgb: 0.19, 0.19, 0.19
        Rectangle:
            pos: self.pos
            size: self.size

""")


class AddressDisplay(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=1, size_hint_y = 0.15)
        self.add_widget(Label(text=user.address, font_size="40px"))

class ConversionDisplay(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=1)
        self.conversion = Label(text='Conversion', font_size="40px")
        self.add_widget(self.conversion)
        #Clock.schedule_interval(self.getConversion, 1)

    def getConversion(self, dt):
        newconversion = getTRXtoUSD()
        self.conversion.text = str(newconversion)

class TronPowerDisplay(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=1)
        self.tronpower = Label(text='TronPower', font_size="40px")
        self.add_widget(self.tronpower)
        #Clock.schedule_interval(self.getBalance, 1)

    def getBalance(self, dt):
        newbalance = getformattedBalance(user.address)
        self.tronpower.text = str(newbalance)

class BalanceDisplay(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=1)
        self.balance = Label(text='SomeNumber', font_size="40px")
        self.add_widget(self.balance)
        #Clock.schedule_interval(self.getBalance, 1)

    def getBalance(self, dt):
        newbalance = getformattedBalance(user.address)
        self.balance.text = str(newbalance)

class MidDisplay(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=3, rows=1, size_hint_y = 0.20)
        self.spacing = SPACING
        self.add_widget(BalanceDisplay())
        self.add_widget(ConversionDisplay())
        self.add_widget(TronPowerDisplay())


class ToAddressBlocks(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=1)


class FromAddressBlocks(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=1)

class BlocksDisplay(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=2, rows=1)
        self.spacing = SPACING
        self.add_widget(ToAddressBlocks())
        self.add_widget(FromAddressBlocks())


class WalletPage(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=3)
        self.padding = SPACING
        self.spacing = SPACING
        self.add_widget(AddressDisplay())
        self.add_widget(MidDisplay())
        self.add_widget(BlocksDisplay())
