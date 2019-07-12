# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    def __str__(self):
        return f"{self.name}. {self.description}"
    def next(self, direction):
        if direction == 'w': #w is north/up
            return self.n_to
        elif direction == 'a': #a is east/left
            return self.e_to
        elif direction == 's': #s is south/down
            return self.s_to
        elif direction == 'w': #w is west/right
            return self.w_to
        else:
            return None
    def retrieveItems(self, itemName):
        for item in self.items:
            if item.name == itemName:
                return item
        return None