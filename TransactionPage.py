import tkinter as tk
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Frame
from Bill import *
from Item import *


class TransactionPage(Frame):

    def __init__(self, *args, **kwargs):

        # Call parent constructor
        tk.Frame.__init__(self, padx = 100, pady = 100, *args, **kwargs)

        self.bill = Bill()

        self.ledger = Frame(self, width=700, height=900)
        self.ledger.grid(row = 0, column=2, rowspan=3, padx = 50, pady = 50)

        self.sumlabel = Label(self, text="Sum").grid(row = 4, column = 2)
        self.sumprice = Label(self, text="$0.00").grid(row = 5, column = 2)

        Label(self, text = "Item Name").grid(row=0)
        self.item = Entry(self)
        self.item.grid(row=0, column=1, padx = 50, pady = 50)

        Label(self, text = "Quantity").grid(row=1)
        self.quantity = Entry(self)
        self.quantity.grid(row=1, column=1, padx = 50, pady = 50)

        self.additem = Button(self, text="Add Item", command=self.addaction)
        self.additem.grid(row=2, column=1, padx = 50, pady = 50)

    def addaction(self):
        name = self.item.get()
        quantity = self.quantity.get()
        item = Item(name, quantity)
        info = name + "                 " + quantity + "                " + str(float(item.price)*float(item.quantity))
        Label(self.ledger, text=info).pack()

        self.bill.add(item)
        self.sumprice = Label(self, text=str(self.bill.sum)).grid(row = 5, column = 2)

    def show(self):

        self.lift()