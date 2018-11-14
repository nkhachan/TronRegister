import tkinter as tk
from tkinter import Entry

class LoginPage(tk.Frame):

    def __init__(self, *args, **kwargs):

        # Call parent constructor
        tk.Frame.__init__(self, *args, **kwargs)

        username = Entry(self)
        username.pack(side="top", expand=True)

    def show(self):

        self.lift()