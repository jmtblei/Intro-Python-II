class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return self.name
    def canEquip(self):
        return False

class Equipment(Item):
    def __init__(self, name, description, powerLevel):
        super().__init__(name, description)
        self.powerLevel = powerLevel
    def canEquip(self):
        return True