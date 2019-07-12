class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return self.name
    def canEquip(self):
        return False
    def takeItem(self):
        print(f"You picked up {self.name}\n----------")
    def dropItem(self):
        print(f"You discarded {self.name}\n----------")