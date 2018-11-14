import tkinter as tk
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import Text
from TronAPI import *
import time


class LoginPage(tk.Frame):

    def __init__(self, *args, **kwargs):

        # Call parent constructor
        tk.Frame.__init__(self, *args, **kwargs)

        self.username = Entry(self)
        self.username.grid(row=0, column=0, padx = 20, pady = 20)

        self.submit = Button(self, text="Submit", command=self.submitAddress)
        self.submit.grid(row=1, column=0, padx = 20, pady = 20)

    def submitAddress(self):
        address = self.username.get()
        if (len(address) == 34):
            self.username.grid_forget()
            self.submit.grid_forget()

            cachedhashes = []

            balance = str(getbalance(address))

            if (balance != str(False)):
                self.text = Text(self, height=2, width=30)
                self.text.pack()
                Label(text="Your current balance is : " + str(formatBalance(balance)) + "TRX\n").pack()
                Label(text="Your most recent transactions are the following \n ").pack()
                for transaction in gettransactionobjects(address):
                    cachedhashes.append(transaction.hash)
                    Label(text=transaction).pack()

            else:
                Label(text="You have no balance in your account").grid()

            '''
            while (1):
                time.sleep(2)

                newtransactions = gettransactionobjects(address)
                if (newtransactions):

                    if (len(newtransactions) > len(cachedhashes)):
                        pass

                    else:
                        lastTransaction = getlasttransactionobject(address)
                        if (lastTransaction.hash not in cachedhashes):
                            Label(text=lastTransaction).pack()
                            cachedhashes.append(lastTransaction.hash)'''

    def show(self):
        self.lift()