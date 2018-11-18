from kivy.uix.gridlayout import GridLayout
from kivy.uix.bubble import Bubble
from kivy.uix.bubble import BubbleButton
from kivy.lang import Builder
from kivy.uix.image import Image


Builder.load_string("""
<MainPage>:
  bcolor: 1, 1, 1, 1
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
      
""")

class WalletImage(Image):
    def __init__(self, **kwargs):
        super(WalletImage, self).__init__(**kwargs)
        self.source = "wallet.png"
        self.center_x = 50
        self.center_y = 50

class TransactionImage(Image):
    def __init__(self, **kwargs):
        super(TransactionImage, self).__init__(**kwargs)
        self.source = "transaction.png"
        self.center_x = 50
        self.center_y = 150

class WalletBubbleButton(BubbleButton):
    def __init__(self, **kwargs):
        super(WalletBubbleButton, self).__init__(**kwargs)
        self.add_widget(WalletImage())

class TransactionBubbleButton(BubbleButton):
    def __init__(self, **kwargs):
        super(TransactionBubbleButton, self).__init__(**kwargs)
        self.add_widget(TransactionImage())


class SideBubble(Bubble):
    def __init__(self, **kwargs):
        super(SideBubble, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (None, None)
        self.size = (100, 200)
        self.arrow_pos = "right_mid"
        self.add_widget(WalletBubbleButton())
        self.add_widget(TransactionBubbleButton())

class MainPage(GridLayout):

    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.add_widget(SideBubble())