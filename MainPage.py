import tkinter as tk
from LoginPage import *
from TransactionPage import *

class MainPage(tk.Frame):

    def __init__(self, *args, **kwargs):

        # Call parent constructor
        tk.Frame.__init__(self, *args, **kwargs)

        # Create pages
        lpage = LoginPage(self)
        tpage = TransactionPage(self)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        lpage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        tpage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        buttonframe = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)

        lbutton = tk.Button(buttonframe, text="Login", command=lpage.lift)
        tbutton = tk.Button(buttonframe, text="Transaction", command=tpage.lift)

        lbutton.pack(side="left")
        tbutton.pack(side="left")

        lpage.show()
