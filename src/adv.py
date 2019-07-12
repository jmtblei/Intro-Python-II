from room import Room
from player import Player
from item import Item
from item import Equipment

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

#Declare items

# item = {
#     'torch': Item("Torch", "A burning torch, it lights up the area granting you more vision."),
#     'stick': Weapon("Stick", "A long stick; you can poke things with it.", "weapon", 5),
#     'longsword': Weapon("Long Sword", "A sharp long sword; this can do some damage.", "weapon", 50),
#     'woodenshield': Armor("Wooden Shield", "A wooden shield; it's pretty durable.", "armor", 30),
#     'oldboots': Armor("Old Boots", "A pair of old boots; at least they fit!", "armor", 10)
# }
torch = Item("Torch", "A burning torch, it lights up the area granting you more vision."),
stick = Equipment("Stick", "A long stick; you can poke things with it.", 5),
longsword = Equipment("Long Sword", "A sharp long sword; this can do some damage.", 50),
woodenshield = Equipment("Wooden Shield", "A wooden shield; it's pretty durable.", 30),
oldboots = Equipment("Old Boots", "A pair of old boots; at least they fit!", 10)

room['outside'].items.append(torch)
room['foyer'].items.append(stick)
room['overlook'].items.append(oldboots)
room['narrow'].items.append(woodenshield)
room['treasure'].items.append(longsword)


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input("Enter your player name: ")
newPlayer = Player(name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(newPlayer)
    controls = input("What would you like to do? ")
    if controls == 'q':
        print(f"{newPlayer.name} has quit")
        break
    elif controls == 'h':
        print("Navigate using WASD\n Press E to examine the room\n Press Q to exit the game")
    elif controls in ['w', 'a', 's', 'd']:
        newPlayer.move(controls)
    else:
        print(f"Invalid command input. press H for help")
