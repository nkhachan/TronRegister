from sys import exit
from tkinter import *


class Window(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.bg = "black"


class WalletButton(Button):
    def __init__(self, parent=None):
        Button.__init__(self, parent, text='Wallet')
        self.command = exit

class TransButton(Button):
    def __init__(self, parent=None):
        Button.__init__(self, parent, text='$')
        self.command = exit

def runApp():
    parent = Frame(None)

    parent.pack()
    Window(parent).pack(side=RIGHT)
    WalletButton().pack(side=LEFT, padx=20, pady=20)
    TransButton().pack(side=LEFT, padx = 20, pady = 20)
    parent.mainloop()