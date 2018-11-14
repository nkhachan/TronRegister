
class Inventory:

    def __init__(self):
        with open('localdata/inventory.json', 'r') as myfile:
            self.data = json.loads(myfile.read())


inventory = Inventory()