from room import Room
from player import Player
from item import Item

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

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Declare items

torch = Item("torch", "A burning torch, it lights up the area granting you more vision.")
stick = Item("stick", "A long stick; you can poke things with it.")
longsword = Item("sword", "A sharp long sword; this can do some damage.")
woodenshield = Item("shield", "A wooden shield; it's pretty durable.")
oldboots = Item("boots", "A pair of old boots; at least they fit!")

room['outside'].items.append(torch)
room['foyer'].items.append(stick)
room['overlook'].items.append(oldboots)
room['narrow'].items.append(woodenshield)
room['treasure'].items.append(longsword)


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
    print(f"You look around and see a {newPlayer.room.items}")
    print(f'Your current inventory: {newPlayer.inventory}\n')
    # controls = input("What would you like to do? ")
    # if controls == 'q':
    #     print(f"**{newPlayer.name} has quit**")
    #     break
    # elif controls == 'h':
    #     print("- Navigate using WASD\n- Press I to check your inventory\n- Press Q to exit the game")
    # elif controls == 'i':
    #     print(f"**You currently have {newPlayer.inventory} in your inventory**")
    # elif controls in ['w', 'a', 's', 'd']:
    #     newPlayer.move(controls)
    # else:
    #     print(f"**Invalid command input. press H for help**")
    
    action = input('**Please take or discard items. e.g. "take (item)" or "drop (item)" (no quotes, no parenthesis)**:')
    command = action.split(" ")

    if command[0] == "take":
        item = newPlayer.room.retrieveItems(command[1])
        if item == None:
            print("No such item here.\n----------")
        else:
           newPlayer.room.items.remove(item)
           newPlayer.inventory.append(item)
           item.takeItem()
    elif command[0] == "drop":
        item = newPlayer.retrieveItems(command[1])
        if item == None:
            print("I'm not holding that in my inventory.\n----------")
        else:
            newPlayer.room.items.append(item)
            newPlayer.inventory.remove(item)
            item.dropItem()
    else:
        print(f"I guess I'll ignore this item and come back later...\n----------")
    controls = input("Which direction do you want to go (WASD)? ")
    if controls == 'q':
        print(f"**{newPlayer.name} has quit**")
        break
    elif controls == 'h':
        print('"- Navigate using WASD\n- Take or discard items by inputing "take (item)" or "drop (item)" (no parenthesis)\n- Press Q to exit the game"')
    elif controls in ['w', 'a', 's', 'd']:
        newPlayer.move(controls)
    else:
        print(f"**Invalid command input. press H for help**\n----------")