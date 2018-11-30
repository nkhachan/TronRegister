import sys
import os
sys.path.append(os.getcwd() + "/../src")
from PyQt4 import QtGui, QtCore
from User import user
from Binance import *
from TronAPI import *
from Inventory import *

WINDOW_SIZE = 1000

class InventoryList(QtGui.QWidget):
    def __init__(self, parent=None):
        super(InventoryList, self).__init__(parent)
        self.setStyleSheet("""QListWidget{background:QColor(200,100,150);}""")
        self.chosenItem = "DummyItem"

        self.list = QtGui.QListWidget(self)
        self.list.setStyleSheet("background-color: (255, 0, 0)")
        self.list.itemClicked.connect(self.choose)
        self.fillInventory()

        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(self.list)

    def choose(self, item):
        self.chosenItem = item.text()

    def fillInventory(self):
        for item in inventory.items:
            self.list.addItem(item)



class TransGrid(QtGui.QGridLayout):
    def __init__(self, parent=None):
        super(TransGrid, self).__init__(parent)
        self.list = InventoryList()
        self.addWidget(self.list)

        self.quantity = QtGui.QLineEdit()
        self.addWidget(self.quantity)

        self.addItemButton = QtGui.QPushButton("Push")
        self.addItemButton.clicked.connect(self.addProduct)
        self.addItemButton.setStyleSheet("color: (130, 224, 170)")
        self.addWidget(self.addItemButton)


    def addProduct(self):
        print(self.list.chosenItem, self.quantity.text())


class WalletGrid(QtGui.QGridLayout):
    def __init__(self, parent=None):
        super(WalletGrid, self).__init__(parent)

        self.address = QtGui.QLabel(user.address)

        self.balance = QtGui.QLabel("Some amount")
        self.power = QtGui.QLabel("Some other amount")
        self.exchange = QtGui.QLabel(str(getTRXtoUSD()))

        self.toBox = QtGui.QLabel("toBox")
        self.fromBox = QtGui.QLabel("fromBox")

        self.addWidget(self.address, 0, 0, 1, 6)
        self.addWidget(self.balance, 1, 0, 1, 2)
        self.addWidget(self.power, 1, 2, 1, 2)
        self.addWidget(self.exchange, 1, 4, 1, 2)
        self.addWidget(self.toBox, 2, 0, 3, 3)
        self.addWidget(self.fromBox, 2, 3, 3, 3)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateWallet)
        self.timer.start(1000)

        self.setSpacing(30)

        self.address.setStyleSheet('.QLabel{{background: rgb({}, {}, {});}}'.format(130, 224, 170))
        self.balance.setStyleSheet('.QLabel{{background: rgb({}, {}, {});}}'.format(22, 160, 133))
        self.power.setStyleSheet('.QLabel{{background: rgb({}, {}, {});}}'.format(22, 160, 133))
        self.exchange.setStyleSheet('.QLabel{{background: rgb({}, {}, {});}}'.format(22, 160, 133))
        self.toBox.setStyleSheet('.QLabel{{background: rgb({}, {}, {});}}'.format(133, 193, 233))
        self.fromBox.setStyleSheet('.QLabel{{background: rgb({}, {}, {});}}'.format(133, 193, 233))

    def updateWallet(self):
        self.balance.setText(str(getformattedBalance(user.address)))
        self.exchange.setText(str(getTRXtoUSD()))


class MainWidget(QtGui.QTabWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setStyleSheet("background-color:#313131;")
        self.setGeometry(0, 0, WINDOW_SIZE + 500, WINDOW_SIZE)

        self.setTabPosition(2)

        self.walletwidget = QtGui.QWidget()
        self.walletwidget.setStyleSheet("background-color: (44, 62, 80)")
        self.transwidget = QtGui.QWidget()

        WalletGrid(self.walletwidget)
        TransGrid(self.transwidget)


        self.addTab(self.walletwidget, "Transaction")
        self.addTab(self.transwidget, "Wallet")
        self.show()



class MainApp(QtGui.QApplication):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)

def runApp():
    app = MainApp(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec_())
