import sys
import os
sys.path.append(os.getcwd() + "/../src")
from Bill import bill
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

SPACING = 25

Builder.load_string("""
<TransactionPage>
    canvas.before:
        Color:
            rgb: 0.14, 0.14, 0.14
        Rectangle:
            pos: self.pos
            size: self.size
            
<AddItemsBar>
    canvas.before:
        Color:
            rgb: 0.19, 0.19, 0.19
        Rectangle:
            pos: self.pos
            size: self.size

<FinishTransPage>
    canvas.before:
        Color:
            rgb: 0.19, 0.19, 0.19
        Rectangle:
            pos: self.pos
            size: self.size

""")


class ItemQuantityBar(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=2, rows=1)
        self.spacing = SPACING
        self.item = TextInput(text='Item', font_size=30)
        self.quantity = TextInput(text='Quantity', font_size=30)

        self.add_widget(self.item)
        self.add_widget(self.quantity)

    def getitem(self):
        return self.item.text

    def getquantity(self):
        return self.quantity.text


class AddItemsBar(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=4)
        self.add_widget(Button(text="Add Item", font_size=30, on_press=parent.additem))


class FinishTransBar(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=4)
        self.add_widget(Button(text="Submit Transaction", font_size=30, on_press=self.finishtransaction))

    def finishtransaction(self, dt):
        bill.billtoprinter()
        self.parent.updateTally()

class AddItems(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, rows=4)
        self.spacing = SPACING
        self.itemquantity = ItemQuantityBar()

        self.add_widget(self.itemquantity)
        self.add_widget(AddItemsBar(self))
        self.add_widget(FinishTransBar())

    def additem(self, callback):
        bill.add(self.itemquantity.getitem(), self.itemquantity.getquantity())
        bill.printBill()
        self.parent.updateTally()

    def updateTally(self):
        self.parent.updateTally()


class Tally(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=1, size_hint_x = 0.7)
        self.total = Label(text="Tally", font_size = 30)
        self.add_widget(self.total)

    def update(self):
        self.total.text = bill.toString()

class TransactionPage(GridLayout):
    def __init__(self, parent=None):
        super().__init__(cols=2, rows=1)
        self.padding = SPACING
        self.spacing = SPACING
        self.additems = AddItems()
        self.tally = Tally()

        self.add_widget(self.additems)
        self.add_widget(self.tally)

    def updateTally(self):
        self.tally.update()
