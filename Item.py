from Inventory import inventory

'''

    Item is a single type of item in the bill

    Contains :
        Name of Item
        Quantity
'''
import json

class Item:

    def __init__(self, name, quantity):
        self.name     = name
        self.quantity = quantity
        if name in inventory.items:
            self.price = inventory.items[name]
        else:
            raise LookupError("This Item does not have a price!")

    def add(self, quantity):
        self.quantity += quantity


    def sub(self, quantity):
        self.quantity -= quantity