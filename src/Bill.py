'''

    Bill

'''
from Item import *
from QRCode import *
from User import user

class Bill:

    def __init__(self):
        self.items = {}
        self.sum = 0

    def add(self, name, quantity):
        if (name in self.items.keys()):
            self.items[name].add(quantity)
        else :
            self.items[name] = Item(name, quantity)
        self.sum += float(quantity)*float(self.items[name].price)

    #def add(self, item):
     #   if (item.name in self.items.keys()):
      #      self.items[item.name].add(item.quantity)
       # else :
       #     self.items[item.name] = item
       # self.sum += float(item.quantity)*float(self.items[item.name].price)

    def printBill(self):
        print(self.toString())

    def toString(self):
        billstring = ""
        for item in self.items:
            name = self.items[item].name
            length = len(name)
            billstring += name +  " "*(40-length) +  self.items[item].quantity +  " x "  +  str(self.items[item].price) + "\n"

        return billstring

    def billtoprinter(self):
        qrcode = createQR(user.address)
        self.clearbill()


    def clearbill(self):
        self.items = {}
        self.sum = 0

bill = Bill()