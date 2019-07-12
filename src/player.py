# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []
    def __str__(self):
        return f"----------\n{self.name} is currently in {self.room}"
    def move(self, direction):
        nextRoom = self.room.next(direction)
        if nextRoom is not None:
            self.room = nextRoom
        else: 
            print("**This is a dead end.**\n----------")
    def retrieveItems(self, itemName):
        for item in self.inventory:
            if item.name == itemName:
                return item
        return None