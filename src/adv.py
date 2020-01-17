from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [
                         Item("lantern", "A tatered lantern with little oil in it"),
                     ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [
        Item("Coins", "Golden coins that are slightly beaten"),
    ]),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

# Create a player
# Let player input their name

player = Player(input("Please enter your name: "), room['outside'])


directions = ["n", "s", "e", "w"]
actions = ["get", "drop", 'take']
# Create basic REPL loop


def player_options():
    print(
        """
=================================options====================================

q: quit
n/s/e/w: Move north, south, east or west to the next room
i: display inventory
get <item>: add item to inventory
drop <item>: rmove item from inventory, items dropped will stay in the room

============================================================================
\n
"""
    )


while True:
    # Get the items in the room
    print(player.current_room)
    player.current_room.get_items()
    # Read command
    # cmd = input("~~> ").lower()
    print("Enter h for help")
    cmd = input("What would you like to do: ").lower().split(" ")

    # player moves
    if len(cmd) == 1:
        # Check if it's n/s/e/w/q
        if cmd[0] in directions:
            # Make player travel in that direction
            player.travel(cmd[0])
        elif cmd[0] == "h":
            # show options
            player_options()
        elif cmd[0] == "i":
            # show player inventory
            player.get_inventory()
        elif cmd[0] == "q":
            # Quit
            print("Goodbye!")
            exit()
        else:
            print("I did not recognize that command")
    # get take drop item
    elif len(cmd) == 2:
        if cmd[0] in actions:
            print("ACTION: ", cmd[0])

            if cmd[0] == 'get' or cmd[0] == 'take':
                room_item = [
                    item.name for item in player.current_room.items if item.name == cmd[1]
                ]

                if len(room_item) == 1:
                    player.get_item(room_item[0])
                else:
                    print("Sorry that item is not in the current room")
            elif cmd[0] == 'drop':

                player_item = [
                    item.name for item in player.inventory if item.name == cmd[1]
                ]
                if len(player_item) == 1:
                    player.drop_item(player_item[0])
                else:
                    print("Sorry that item is not in inventory")
        else:
            print("I did not recognize that command")
    else:
        print("I did not recognize that command")
