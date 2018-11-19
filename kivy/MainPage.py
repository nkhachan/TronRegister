from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from TransactionPage import TransactionPage
from WalletPage import WalletPage


class WalletImage(Image):
    def __init__(self, **kwargs):
        super(WalletImage, self).__init__(**kwargs)
        self.source = "wallet.png"

class WalletButton(ButtonBehavior, Image):
    def __init__(self, parent=None):
        super().__init__()
        self.source = "img/wallet.png"

    def on_press(self):
        self.parent.switchToWallet()

class TransButton(ButtonBehavior, Image):
    def __init__(self, parent=None):
        super().__init__()
        self.source = "img/trans.png"

    def on_press(self):
        self.parent.switchToTrans()

class SidePanelButtons(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=3, size_hint_y = 0.25)
        #walletbutton = Button(text='Wallet', on_press=parent.switchToWallet)
        #transbutton = Button(text='Transaction', on_press=parent.switchToTrans)
        #self.add_widget(walletbutton)
        #self.add_widget(transbutton)

        self.add_widget(WalletButton(self))
        self.add_widget(TransButton(self))

    def switchToWallet(self, callback=None):
        self.parent.switchToWallet(callback)

    def switchToTrans(self, callback=None):
        self.parent.switchToTrans(callback)


class SidePanel(GridLayout):
    def __init__(self, parent=None, **kwargs):
        super().__init__(cols=1, rows=3, size_hint_x = 0.10, **kwargs)
        self.add_widget(SidePanelButtons(self))
        self.add_widget(Label(text=""))

    def switchToWallet(self, callback):
        self.parent.switchToWallet()

    def switchToTrans(self, callback):
        self.parent.switchToTrans()


class MainPanel(GridLayout):
    def __init__(self, parent=None, **kwargs):
        super(**kwargs).__init__(cols=1, rows=3)
        self.id="Fuck me"
        self.transPage = TransactionPage()
        self.walletPage = WalletPage()
        self.add_widget(self.walletPage)

    def switchToWallet(self):
        if isinstance(self.children[0], TransactionPage):
            self.remove_widget(self.transPage)
            self.add_widget(self.walletPage)

    def switchToTrans(self):
        if isinstance(self.children[0], WalletPage):
            self.remove_widget(self.walletPage)
            self.add_widget(self.transPage)


class MainPage(GridLayout):
    def __init__(self, parent=None, **kwargs):
        super(MainPage, self).__init__(**kwargs, cols = 2)
        self.add_widget(SidePanel())
        self.add_widget(MainPanel())


    def switchToWallet(self):
        self.children[0].switchToWallet()

    def switchToTrans(self):
        self.children[0].switchToTrans()
