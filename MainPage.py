import tkinter as tk
from tkinter import ttk
from LoginPage import *
from TransactionPage import *

class MainPage(tk.Frame):

    def __init__(self, *args, **kwargs):
        # Call parent constructor
        tk.Frame.__init__(self, *args, **kwargs)

        # Create pages
        lpage = LoginPage(self)
        tpage = TransactionPage(self)

        # Put both of the pages into this Frame container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        lpage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        tpage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # Frame for the buttons on the side bar
        buttonframe = tk.Frame(self, bg = "black", padx = 10, pady = 10)
        buttonframe.pack(side="left", fill="x", expand=True)
        lbutton = tk.Button(buttonframe, text="Login", command=lpage.lift)
        tbutton = tk.Button(buttonframe, text="Transaction", command=tpage.lift)
        lbutton.pack(side="left", padx = 10, pady = 10)
        tbutton.pack(side="left", padx = 10, pady = 10)

        lpage.show()
