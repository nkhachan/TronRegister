from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from TransactionPage import TransactionPage
from WalletPage import WalletPage


class SidePanelButtons(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=2, size_hint_y = 0.25)
        self.add_widget(Button(text='Wallet', on_press=parent.switchToWallet))
        self.add_widget(Button(text='Transaction', on_press=parent.switchToTrans))


class SidePanel(GridLayout):
    def __init__(self, parent=None, **kwargs):
        super().__init__(cols=1, rows=3, size_hint_x = 0.15, **kwargs)
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
