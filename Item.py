'''

    Item is a single type of item in the bill

    Contains :
        Name of Item
        Quantity
'''

class Item:

    def __init__(self, name, quantity):
        self.name     = name
        self.quantity = quantity


    def add(self, quantity):
        self.quantity += quantity


    def sub(self, quantity):
        self.quantity -= quantity